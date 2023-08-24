from collections import abc
import enchant
from typing import Iterator, Optional

class Dictionary(abc.Mapping):
    def __init__(self) -> None:
        self.d = enchant.Dict("en_US")
    def __getitem__(self, __key: str) -> bool:
        return self.d.check(__key)
    def __len__(self) -> int:
        return 1
    def __iter__(self) -> Iterator[Optional[str]]:
        return iter([None])
