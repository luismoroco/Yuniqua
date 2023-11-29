from typing import Dict
from sqlalchemy import Column, String, BigInteger, ForeignKey

from src.yuniqua.database.model import SupportedLanguage, EditorState
from .base import Base

__all__ = ["SessionEditor"]


class SessionEditor(Base):
    __tablename__ = "session_editor"

    session_editor_id = Column(BigInteger(), autoincrement=True, primary_key=True)
    name = Column(String(), nullable=False)
    access_token = Column(String(), nullable=False)
    language_id = Column(
        BigInteger(),
        ForeignKey("supported_language.supported_language_id"),
        nullable=False,
    )
    state_id = Column(
        BigInteger(), ForeignKey("editor_state.editor_state_id"), nullable=False
    )

    def to_json(self) -> Dict:
        return {
            "name": self.name,
            "access_token": self.access_token,
            "language": SupportedLanguage(self.language_id),
            "state": EditorState(self.state_id),
        }
