from abc import ABC, abstractmethod
from typing import Iterator, Optional

from ciphers import Cipher
from confirmation.confirmation import Confirmation

class Analyze(ABC):
    @abstractmethod
    def decode(self, decoder: Iterator[Cipher],  confirmer: Confirmation, to_decode: str) -> Optional[tuple[str, int]]:
        pass

from .brute import Brute
