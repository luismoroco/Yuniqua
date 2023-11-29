import abc
from typing import Optional

from sqlalchemy import and_

from src.yuniqua.database import EditorUser
from src.yuniqua.database.db import DBModule

__all__ = ["UserRepository", "UserPostgresRepository"]


class UserRepository(abc.ABC):
    @abc.abstractmethod
    def get_user(
        self, username: str, password: Optional[str] = None
    ) -> Optional[EditorUser]:
        raise NotImplementedError

    @abc.abstractmethod
    def create_user(self, username: str, password: str) -> EditorUser:
        raise NotImplementedError


class UserPostgresRepository(UserRepository, DBModule):
    def __init__(self):
        super().__init__()

    def get_user(
        self, username: str, password: Optional[str] = None
    ) -> Optional[EditorUser]:
        where = [EditorUser.username == username]

        if password:
            where.append(EditorUser.password == password)

        return self.session.query(EditorUser).filter(*where).one_or_none()

    def create_user(self, username: str, password: str) -> EditorUser:
        new_user = EditorUser()
        new_user.username = username
        new_user.password = password

        self.session.add(new_user)
        self.session.commit()

        return new_user
