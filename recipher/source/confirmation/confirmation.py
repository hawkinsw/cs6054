from .dictionary import Dictionary
class Confirmation:
    def __init__(self, dnary: Dictionary, separator: str = " ") -> None:
        self.dnary = dnary
        self.separator = separator
        pass
    def confirm(self, to_confirm: str) -> bool:
        words_to_confirm: list[str] = to_confirm.split(self.separator)
        for word_to_confirm in words_to_confirm:
            if word_to_confirm == '' or not self.dnary[word_to_confirm]:
                return False
        return True