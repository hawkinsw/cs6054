from typing import TypeVar, Tuple, List
from math import gcd as gcd_native
from random import randint
from PyRandLib import FastRand32

T = TypeVar("T")

def swap(a: T, b: T) -> Tuple[T, T]:
    return (b, a)

def gcd_r_lindio(a: int, b: int, debug: bool = False) -> Tuple[int, Tuple[int, int]]:
    return gcd_r_lindio_helper(a, b, (1, 0), (0, 1), debug)

def gcd_r_lindio_helper(a: int, b: int, rs2: Tuple[int, int], rs1: Tuple[int, int], debug: bool = False) -> Tuple[int, Tuple[int, int]]:
    if debug:
        print(f"gcd({a}, {b})")
        print(f"{rs2=}")
        print(f"{rs1=}")
    if b > a:
        a, b = swap(a,b)

    if b == 0:
        return (a, rs2)

    close: int = a // b
    remainder: int = a % (b * close)

    (r2, s2) = rs2
    (r1, s1) = rs1
    rs = (r2 - close * r1, s2 - close * s1)

    return gcd_r_lindio_helper(b, remainder, rs1, rs, debug=debug)

def gcd_r(a: int, b: int, debug: bool = False) -> int:
    if b > a:
        a, b = swap(a,b)

    if b == 0:
        return a

    guess: int = a // b
    remainder: int = a % (b * guess)

    return gcd_r(b, remainder, debug=debug)

def gcd_i(a: int, b: int, debug: bool = False) -> int:
    if b > a:
        a, b = swap(a,b)

    while b != 0:
        if debug:
            print(f"gcd({a}, {b})")
        guess: int = a // b
        remainder = a % (b * guess)

        a = b
        b = remainder

    return a

def testcases(quantity: int) -> List[Tuple[Tuple[int, int], int]]:
    results: List[Tuple[Tuple[int, int], int]] = []
    #randomizer = FastRand32()
    #randomizer = FastRand32()
    for _ in range(quantity):
        a = randint(1000, 1000000)
        b = randint(1000, 1000000)
        results.append(((a,b), gcd_native(a,b)))
    return results