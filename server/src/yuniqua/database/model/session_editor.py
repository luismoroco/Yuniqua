from typing import Dict

from sqlalchemy import Column, String, BigInteger, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship, Mapped

from src.yuniqua.database.model import SupportedLanguage, EditorState, YuniquaUser
from .base import Base

__all__ = ["Editor"]


class Editor(Base):
    __tablename__ = "session_editor"

    session_editor_id = Column(BigInteger(), autoincrement=True, primary_key=True)
    name = Column(String(), nullable=False)
    access_token = Column(String(), nullable=False)
    max_connections = Column(Integer())
    user_owner_id = Column(
        BigInteger(),
        ForeignKey("yuniqua_user.user_id"),
        nullable=False,
    )
    language_id = Column(
        BigInteger(),
        ForeignKey("supported_language.supported_language_id"),
        nullable=False,
    )
    state_id = Column(
        BigInteger(), ForeignKey("editor_state.editor_state_id"), nullable=False
    )
    created_at = Column(DateTime())

    _date_format = "%Y-%m-%d %H:%M:%S"

    owner: Mapped["YuniquaUser"] = relationship(
        "YuniquaUser",
        back_populates="session_editors",
    )

    def _get_formatted_date(self) -> str:
        return self.created_at.strftime(self._date_format)

    def to_json(self) -> Dict:
        return {
            "name": self.name,
            "access_token": self.access_token,
            "max_connections": self.max_connections,
            "user_owner_id": self.user_owner_id,
            "language": SupportedLanguage(self.language_id),
            "state": EditorState(self.state_id),
            "created_At": self._get_formatted_date(),
        }
