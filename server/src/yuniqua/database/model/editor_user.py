from typing import Dict
from sqlalchemy import Column, String, BigInteger

from .base import Base

__all__ = ["EditorUser"]


class EditorUser(Base):
    __tablename__ = "editor_user"

    editor_user_id = Column(BigInteger(), primary_key=True, autoincrement=True)
    username = Column(String(), nullable=False)
    password = Column(String(), nullable=False)

    def to_json(self) -> Dict:
        return {"username": self.username, "editor_user_id": self.editor_user_id}
