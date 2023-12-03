from typing import Dict

from sqlalchemy import Column, String, BigInteger, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship, Mapped

from src.yuniqua.database.model import (
    SupportedLanguageType,
    EditorStateType,
    YuniquaUser,
)
from .base import Base

__all__ = ["Editor"]


class Editor(Base):
    __tablename__ = "session_editor"

    session_editor_id = Column(BigInteger(), autoincrement=True, primary_key=True)
    name = Column(String(), nullable=False)
    access_token = Column(String(), nullable=False)
    max_connections = Column(Integer())
    user_owner_id = Column(
        Integer(),
        ForeignKey("yuniqua_user.user_id"),
        nullable=False,
    )
    language_id = Column(
        Integer(),
        ForeignKey("supported_language.supported_language_id"),
        nullable=False,
    )
    state_id = Column(
        Integer(),
        ForeignKey("editor_state.editor_state_id"),
        nullable=False,
    )
    created_at = Column(DateTime())

    _date_format = "%Y-%m-%d %H:%M:%S"

    owner: Mapped["YuniquaUser"] = relationship(
        "YuniquaUser",
        back_populates="session_editors",
    )

    def _get_formatted_date(self) -> str:
        return self.created_at.strftime(self._date_format)

    @property
    def language(self) -> str:
        if self.language_id == SupportedLanguageType.PYTHON.value:
            return SupportedLanguageType.PYTHON.name
        elif self.language_id == SupportedLanguageType.PYTHON.value:
            return SupportedLanguageType.CPP.name
        return SupportedLanguageType.JAVASCRIPT.name

    @property
    def status(self) -> str:
        if self.state_id == EditorStateType.ACTIVE.value:
            return EditorStateType.ACTIVE.name
        return EditorStateType.ARCHIVED.name

    def to_json(self) -> Dict:
        return {
            "id": self.session_editor_id,
            "name": self.name,
            "access_token": self.access_token,
            "max_connections": self.max_connections,
            "user_owner_id": self.user_owner_id,
            "language": self.language,
            "state": self.status,
            "created_At": self._get_formatted_date(),
        }
