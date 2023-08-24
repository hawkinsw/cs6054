from . import Cipher
from . import utilities

class Shift(Cipher):
    """
    An implementation of a Shift cipher that meets the requirements
    defined by the :class:`Cipher` ABC.
    """

    a: int
    """ `a` is one of the two private member variables needed to implement the shift cipher. """
    b: int
    def __init__(self, a: int, b: int, m: int) -> None:
        super().__init__()
        self.a = a
        self.b = b
        self.m = m
    def encode(self, to_encode: str) -> str:
        result = ""
        for i in to_encode:
            p =  utilities.char_to_int(i, self.m - 1, ' ')
            c = (p*self.a + self.b) % self.m
            if c < 0:
                c+= self.m
            result += utilities.int_to_char(c, self.m - 1, ' ')
        return result

    def decode(self, to_decode: str) -> str:
        result = ""
        for i in to_decode:
            c =  utilities.char_to_int(i, self.m - 1, ' ')
            p = ((c - self.b)) // self.a % self.m
            if p < 0:
                p += self.m
            result += utilities.int_to_char(p, self.m - 1, ' ')
        return result