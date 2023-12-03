import abc
from typing import Optional, List

from src.yuniqua.database.model import Editor

__all__ = ["EditorRepository"]


class EditorRepository(abc.ABC):
    @abc.abstractmethod
    def get_editor(
        self, access_token: str = None, session_editor_id: int = None
    ) -> Editor:
        raise NotImplementedError

    @abc.abstractmethod
    def list_editors(self, user_id: int, states_ids: List[int]) -> List[Editor]:
        raise NotImplementedError
