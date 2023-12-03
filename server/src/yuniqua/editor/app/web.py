from http import HTTPStatus

from flask import Blueprint, jsonify, request, session

from .request import (
    GetEditorRequest,
    CreateEditorRequest,
    EditEditorRequest,
    DeleteEditorRequest,
    ListEditorRequest,
)
from .usecase import EditorUseCase

__all__ = ["editor_blueprint"]

editor_blueprint = Blueprint("editor", __name__, url_prefix="/editor")


@editor_blueprint.route("", methods=["POST"])
def create_editor():
    if "user_info" not in session:
        return jsonify({"message": "Access denied", "data": None})

    res = EditorUseCase().create_editor(
        CreateEditorRequest(
            **request.get_json(), user_id=session["user_info"]["user_id"]
        )
    )

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND
    return jsonify({"message": "Editor Created", "data": res.to_json()})


@editor_blueprint.route("/<editor_id>", methods=["PUT"])
def edit_editor(editor_id: int):
    res = EditorUseCase().edit_editor(
        EditEditorRequest(**request.get_json(), editor_id=editor_id)
    )

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND
    return jsonify({"message": "OK", "data": res.to_json()})


@editor_blueprint.route("/<editor_id>", methods=["DELETE"])
def delete_editor(editor_id: int):
    res = EditorUseCase().delete_editor(DeleteEditorRequest(editor_id=editor_id))

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND
    return jsonify({"message": "OK", "data": None})


@editor_blueprint.route("/<user_id>", methods=["GET"])
def list_editors(user_id: int):
    res = EditorUseCase().list_editors(ListEditorRequest(user_id=user_id))

    return jsonify({"message": "OK", "data": [editor.to_json() for editor in res]})


@editor_blueprint.route("/<token_access>", methods=["GET"])
def get_editor(token_access: str):
    res = EditorUseCase().get_editor(GetEditorRequest(access_token=token_access))

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND
    return jsonify({"message": "OK", "data": res.to_json()})
