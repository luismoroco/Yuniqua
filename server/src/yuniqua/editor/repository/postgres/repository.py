from typing import Optional

from src.yuniqua.database.model import Editor
from src.yuniqua.database.db import DBModule
from src.yuniqua.editor.repository.abc import EditorRepository

__all__ = ["EditorPostgresRepository"]


class EditorPostgresRepository(DBModule, EditorRepository):
    def get_editor(
        self,
        session_editor_id: Optional[int] = None,
        access_token: Optional[str] = None,
    ) -> Editor:
        where = []

        if session_editor_id:
            where.append(Editor.session_editor_id == session_editor_id)

        if access_token:
            where.append(Editor.access_token == access_token)

        return self.session.query(Editor).filter(*where).one_or_none()
