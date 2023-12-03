import abc
from typing import Optional

from src.yuniqua.database.model import Editor

__all__ = ["EditorRepository"]


class EditorRepository(abc.ABC):
    @abc.abstractmethod
    def get_editor(
        self,
        session_editor_id: Optional[int] = None,
        access_token: Optional[str] = None,
    ) -> Editor:
        raise NotImplementedError
