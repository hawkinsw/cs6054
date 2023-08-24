from confirmation import Confirmation, Dictionary
from ciphers import Cipher, Shift
from analysis import Brute
from typing import Iterator

def bruter() -> Iterator[Cipher]:
    for i in range(0, 27):
        yield Shift(1, i, 27)

def main() -> None:
    dictionary: Dictionary = Dictionary()
    confirmer: Confirmation = Confirmation(dictionary)

    to_encode = 'this a special case'
    s = Shift(1, 4, 27)

    assert(s.decode(s.encode(to_encode)) == to_encode)

    b = Brute()
    result = b.decode(bruter(), confirmer, s.encode(to_encode))
    match result: 
        case (str() as aha, int() as iterations):
            print(f"Got --{aha}-- after {iterations} tries!")
        case _:
            print("Could not decode!")
main()