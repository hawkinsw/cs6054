from linattack import SBox, LinAttack, Input, UnsignedInteger 
from typing import List
EOF = ''

sbox = SBox([0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf],
            [0xe, 0x4, 0xd, 0x1, 0x2, 0xf, 0xb, 0x8, 0x3, 0xa, 0x6, 0xc, 0x5, 0x9, 0x0, 0x7])
tau: List[Input] = []

with open("KPAData.txt") as f:
    l = f.readline()
    count = 0
    while l != EOF and count < 4000:
        count+= 1
        line: List[int] = [int(x) for x in l.rstrip('\n').split()]
        pt: List[int] = []
        ct: List[int] = []
        value: int = 0
        for i in range(0, 4):
            value = UnsignedInteger.FromBits(line[i*4:i*4 + 4])
            pt.append(value)
        for i in range(4, 8):
            value = UnsignedInteger.FromBits(line[i*4:i*4 + 4])
            ct.append(value)
        tau.append(Input(pt, ct))
        l = f.readline()

la = LinAttack(tau, len(tau), sbox.inverse())
(key, guesses) = la.attack()
print(f"{key=}")

# guesses is a 2d array where the indexes are the possible values of the
# sought-after bits and the value is the likelihood the bits are what
# we want. You could easily make some calculations about the variance,
# etc., of these variables -- that would be neat!
print(f"{len(guesses)=}")