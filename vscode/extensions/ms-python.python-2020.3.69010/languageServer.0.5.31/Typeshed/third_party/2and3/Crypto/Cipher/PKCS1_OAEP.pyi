from typing import Any, Optional, Union, Text

from Crypto.PublicKey.RSA import _RSAobj

class PKCS1OAEP_Cipher:
    def __init__(self, key: _RSAobj, hashAlgo: Any, mgfunc: Any, label: Any) -> None: ...
    def can_encrypt(self): ...
    def can_decrypt(self): ...
    def encrypt(self, message: Union[bytes, Text]) -> bytes: ...
    def decrypt(self, ct: bytes) -> bytes: ...


def new(key: _RSAobj, hashAlgo: Optional[Any] = ..., mgfunc: Optional[Any] = ..., label: Any = ...) -> PKCS1OAEP_Cipher: ...
