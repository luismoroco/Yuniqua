from typing import List

from src.yuniqua.database.model import Editor
from src.yuniqua.database.db import session
from src.yuniqua.editor.repository.abc import EditorRepository

__all__ = ["EditorPostgresRepository"]


class EditorPostgresRepository(EditorRepository):
    def get_editor(
        self, access_token: str = None, session_editor_id: int = None
    ) -> Editor:
        where = []

        if access_token:
            where.append(Editor.access_token == access_token)

        if session_editor_id:
            where.append(Editor.session_editor_id == session_editor_id)

        return session.query(Editor).filter(*where).one_or_none()

    def list_editors(self, user_id: int, states_ids: List[int]) -> List[Editor]:
        return (
            session.query(Editor)
            .filter(Editor.user_owner_id == user_id, Editor.state_id.in_(states_ids))
            .all()
        )
