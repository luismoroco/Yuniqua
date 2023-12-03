from typing import Dict, List, TYPE_CHECKING

from sqlalchemy import Column, String, BigInteger, DateTime
from sqlalchemy.orm import relationship, Mapped

from .base import Base

if TYPE_CHECKING:
    from src.yuniqua.database.model import Editor

__all__ = ["YuniquaUser"]


class YuniquaUser(Base):
    __tablename__ = "yuniqua_user"

    user_id = Column(BigInteger(), primary_key=True, autoincrement=True)
    username = Column(String(), nullable=False)
    password = Column(String(), nullable=False)
    alias = Column(String(), nullable=False)
    created_at = Column(DateTime())

    _date_format = "%Y-%m-%d %H:%M:%S"

    session_editors: Mapped[List["Editor"]] = relationship(
        "SessionEditor",
        back_populates="owner",
        cascade="all, delete-orphan",
    )

    def _get_formatted_date(self) -> str:
        return self.created_at.strftime(self._date_format)

    def to_json(self) -> Dict:
        return {
            "user_id": self.user_id,
            "username:": self.username,
            "name": self.alias,
            "created_at": self._get_formatted_date(),
        }
