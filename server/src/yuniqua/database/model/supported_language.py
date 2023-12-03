from enum import Enum

from sqlalchemy import Column, String, BigInteger

from .base import Base

__all__ = ["SupportedLanguageType", "SupportedLanguage"]


class SupportedLanguageType(Enum):
    PYTHON = 1
    CPP = 2
    JAVASCRIPT = 3


class SupportedLanguage(Base):
    __tablename__ = "supported_language"

    supported_language_id = Column(BigInteger(), primary_key=True)
    name = Column(String(), nullable=False)
    label = Column(String(), nullable=False)
