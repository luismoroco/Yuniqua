from typing import Optional
from datetime import datetime

from src.yuniqua.database import YuniquaUser
from src.yuniqua.database.db import DBModule
from src.yuniqua.user.repository.abc import UserRepository

__all__ = ["UserPostgresRepository"]


class UserPostgresRepository(UserRepository, DBModule):
    def __init__(self):
        super().__init__()

    def get_user(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        user_id: Optional[int] = None,
    ) -> Optional[YuniquaUser]:
        """
        Get a user

        :param username:
        :param password:
        :param user_id:
        :return:
        """
        where = []

        if user_id:
            where.append(YuniquaUser.user_id == user_id)

        if username:
            where.append(YuniquaUser.username == username)

        if password:
            where.append(YuniquaUser.password == password)

        return self.session.query(YuniquaUser).filter(*where).one_or_none()

    def delete_user(self, user_id: int) -> None:
        """
        Delete a User

        :param user_id:
        :return:
        """
        (
            self.session.query(YuniquaUser)
            .filter(YuniquaUser.user_id == user_id)
            .delete()
        )
