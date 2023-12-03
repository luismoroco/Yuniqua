import abc
from typing import Optional

from src.yuniqua.database import YuniquaUser

__all__ = ["UserRepository"]


class UserRepository(abc.ABC):
    @abc.abstractmethod
    def get_user(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        user_id: Optional[int] = None,
    ) -> Optional[YuniquaUser]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_user(self, user_id: int) -> None:
        raise NotImplementedError
