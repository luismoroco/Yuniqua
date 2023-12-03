from enum import Enum

from sqlalchemy import Column, String, BigInteger

from .base import Base

__all__ = ["EditorStateType", "EditorState"]


class EditorStateType(Enum):
    ACTIVE = 1
    ARCHIVED = 2


class EditorState(Base):
    __tablename__ = "editor_state"

    editor_state_id = Column(BigInteger(), primary_key=True)
    name = Column(String(), nullable=False)
    label = Column(String(), nullable=False)
