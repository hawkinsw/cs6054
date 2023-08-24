"""
Ciphers
=======

The classes and objects used to implement various cryptographic ciphers.

"""


from abc import ABC, abstractmethod
class Cipher(ABC):
    """ An abstract class that defines required methods that must be 
        implemented in order to be considered a `Cipher`.
    """

    @abstractmethod
    def encode(self, to_encode: str) -> str:
        """
        Encode the given plain-text string `to_encode` and
        return the encoded version.

        :param to_encode: The plain-text string to encode.
        :return: str: The encoded version of the plain text.
        """
        pass 

    @abstractmethod
    def decode(self, to_decode: str) -> str:
        """
        Decode the given cipher-text string `to_decode` and
        return the plain text version.

        :param to_decode: The cipher-text string to encode.
        :return: str: The decoded version of the cipher text.
        """
        pass

from .shift import Shift