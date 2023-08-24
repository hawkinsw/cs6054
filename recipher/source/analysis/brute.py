from . import Analyze
from ciphers import Cipher
from typing import Iterator, Optional 
from confirmation import Confirmation

class Brute(Analyze):
    def decode(self, decoder: Iterator[Cipher],  confirmer: Confirmation, to_decode: str) -> Optional[tuple[str, int]]:
        tries = 0
        for d in decoder:
            result = d.decode(to_decode) 
            tries+=1
            if confirmer.confirm(result):
                return (result, tries)
        return None