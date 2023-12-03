from typing import Dict, Union, List

from .request import (
    CreateEditorRequest,
    EditEditorRequest,
    DeleteEditorRequest,
    ListEditorRequest,
    GetEditorRequest,
)
from src.yuniqua.database.db import DBModule
from src.yuniqua.database.model import Editor, EditorState, SupportedLanguage
from src.yuniqua.user.repository import UserRepository, UserPostgresRepository
from src.yuniqua.editor.repository import EditorRepository, EditorPostgresRepository
from src.yuniqua.services.token import TokenService, TokenBase

__all__ = ["EditorUseCase"]


class EditorUseCase(DBModule):
    user_repository: UserRepository
    token_service: TokenBase
    repository: EditorRepository

    def __init__(self):
        super().__init__()
        self.user_repository = UserPostgresRepository()
        self.token_service = TokenService()
        self.repository = EditorPostgresRepository()

    def create_editor(self, request: CreateEditorRequest) -> Union[Dict, Editor]:
        """
        Create Editor

        :param request:
        :return:
        """
        user = self.user_repository.get_user(user_id=request.user_id)

        if not user:
            return {"message": "User Not Found", "data": None}

        editor = Editor()
        editor.name = request.name
        editor.access_token = self.token_service.generate_token()
        editor.max_connections = request.max_connections
        editor.language_id = SupportedLanguage[request.language].value
        editor.state_id = EditorState["ACTIVE"].value
        editor.owner = user

        self.session.add(editor)
        self.session.commit()

        return editor

    def edit_editor(self, request: EditEditorRequest) -> Union[Dict, Editor]:
        """
        Edit Editor

        :param request:
        :return:
        """
        editor = self.repository.get_editor(session_editor_id=request.editor_id)

        if not editor:
            return {"message": "Editor Not Found", "data": None}

        if request.name:
            editor.name = request.name

        if request.max_connections:
            editor.max_connections = request.max_connections

        if request.language:
            editor.language_id = SupportedLanguage[request.language].value

        self.session.add(editor)
        self.session.commit()

        return editor

    def delete_editor(self, request: DeleteEditorRequest) -> Dict:
        """
        Delete Editor

        :param request:
        :return:
        """
        editor = self.repository.get_editor(session_editor_id=request.editor_id)

        if not editor:
            return {"message": "Editor Not Found", "data": None}

        editor.state_id = EditorState.ARCHIVED.value

        self.session.add(editor)
        self.session.commit()

        return {"message": "Editor Archived", "data": None}

    def list_editors(self, request: ListEditorRequest) -> List[Editor]:
        """
        List Editors

        :param request:
        :return:
        """
        return self.repository.list_editors(
            user_id=request.user_id, states_ids=[EditorState.ACTIVE.value]
        )

    def get_editor(self, request: GetEditorRequest) -> Union[Dict, Editor]:
        """
        Get Editor

        :param request:
        :return:
        """
        editor = self.repository.get_editor(access_token=request.access_token)

        if not editor:
            return {"message": "Editor Not Found", "data": None}

        return editor
