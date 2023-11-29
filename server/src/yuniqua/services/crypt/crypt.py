from src.yuniqua.services.crypt.abc import CryptBase
from src.yuniqua.services.crypt.exc import (
    ObjectForCryptNotProvidedException,
    BadObjectTypeProvidedException,
)
from src.yuniqua.base.crypt import bcrypt

__all__ = ["BcryptService"]


class BcryptService(CryptBase):
    def encrypt(self, **kwargs) -> str:
        if "plain_text" not in kwargs:
            raise ObjectForCryptNotProvidedException

        if not isinstance(kwargs["plain_text"], str):
            raise BadObjectTypeProvidedException

        return bcrypt.generate_password_hash(kwargs["plain_text"]).decode("utf-8")

    def verify(self, **kwargs) -> bool:
        if "hash" not in kwargs or "plain_text" not in kwargs:
            raise BadObjectTypeProvidedException

        return bcrypt.check_password_hash(kwargs["hash"], kwargs["plain_text"])
