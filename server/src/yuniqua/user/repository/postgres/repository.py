from typing import Optional

from src.yuniqua.database import YuniquaUser
from src.yuniqua.database.db import session
from src.yuniqua.user.repository.abc import UserRepository

__all__ = ["UserPostgresRepository"]


class UserPostgresRepository(UserRepository):
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

        return session.query(YuniquaUser).filter(*where).one_or_none()

    def delete_user(self, user_id: int) -> None:
        """
        Delete a User

        :param user_id:
        :return:
        """
        (session.query(YuniquaUser).filter(YuniquaUser.user_id == user_id).delete())
