from typing import NamedTuple, TypeVar, List, Generic, Optional, Tuple

SboxInputType = TypeVar('SboxInputType')
SboxOutputType = TypeVar('SboxOutputType')
_InverseSelf = TypeVar('_InverseSelf', bound='SBox[SboxOutputType, SboxInputType]')

class SBox(Generic[SboxInputType, SboxOutputType]):
    inputs: List[SboxInputType]
    outputs: List[SboxOutputType]

    def __init__(self, inputs: List[SboxInputType], outputs: List[SboxOutputType]):
        self.inputs = inputs
        self.outputs = outputs

    def __call__(self, input: SboxInputType) -> SboxOutputType:
        """ Allows us to treat the SBox as if it were a function that can be called. """
        for i, v in enumerate(self.inputs):
            if v == input:
                return self.outputs[i]
        raise NotADirectoryError()

    def inverse(self) -> _InverseSelf:
        """ Generate an inverse SBox from the current SBox. """
        return SBox(self.outputs, self.inputs)

class Input(NamedTuple):
    plaintext: List[int]
    ciphertext: List[int]

class UnsignedInteger():
    @classmethod
    def FromBits(cls, bits: List[int]) -> int:
        """ Take a list of bits, assume that they represent an unsigned int and calculate that value. """
        value = 0
        lb = len(bits)
        for idx, bv in enumerate(bits):
            value += bv*(2**(lb - 1 - idx))
        return value

class BitField():
    bitCount = 0
    bits: List[int]

    def __init__(self, value: int, bitCount: int):
        # Make sure that the number given to convert to a bitfield fits within
        # the number of bits that we are shown.
        if ( value < 0 or value > (2**bitCount - 1)):
            raise NotImplementedError()

        self.bitCount = bitCount
        self.bits = [0 for _ in range(0, bitCount)]
        for i in range(0, bitCount):
            self.bits[bitCount - 1 - i] = value % 2
            value = value >> 1

    def get(self, idx:int) -> int:
        if (idx > self.bitCount):
            raise NotImplementedError()
        return self.bits[idx]

class LinAttack():
    def __init__(self, tau: List[Input], t: int, inverse: SBox[int, int]):
        self.tau = tau
        self.inverse = inverse
        self.t = t

    def attack(self) -> Tuple[Tuple[int, int], List[List[float]]]:
        count: List[List[float]] = [ [0 for _ in range(0, 0x10)] for _ in range(0, 0x10)]
        for (plain, cipher) in self.tau:
            for l1 in range(0x0, 0x10):
                for l2 in range(0x0, 0x10):
                    y2 = cipher[1]
                    y4 = cipher[3]
                    v42 = y2 ^ l1
                    v44 = y4 ^ l2
                    u42 = self.inverse(v42)
                    u44 = self.inverse(v44)

                    u42b = BitField(u42, 4)
                    u44b = BitField(u44, 4)
                    x1 = BitField(plain[1], 4)

                    z = x1.get(0) ^ x1.get(2) ^ x1.get(3) ^ u42b.get(1) ^ u42b.get(3) ^ u44b.get(1) ^ u44b.get(3)
                    if z == 0:
                        count[l1][l2] += 1
        max = float(-1)
        maxkey: Tuple[int, int] = (0, 0)
        for l1 in range(0x0, 0x10):
            for l2 in range(0x0, 0x10):
                count[l1][l2] = abs(count[l1][l2] - (self.t / 2))
                #print(f"{l1}, {l2} = {count[l1][l2]}")
                if count[l1][l2] > max:
                    max = count[l1][l2]
                    maxkey = (l1, l2)

        return (maxkey, count)