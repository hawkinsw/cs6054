from typing import Any

def char_to_int(character: Any, m: int, space: Any) -> int:
    if ord('a') <= ord(character) and ord(character) <= ord('z'):
        return ord(character) - ord('a')
    if character == space:
        return m
    assert(False)

def int_to_char(c: Any, m: int, space: Any) -> Any:
    if c == m:
        return space
    return chr(c+ ord('a'))