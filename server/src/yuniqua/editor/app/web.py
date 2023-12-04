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
from src.yuniqua.base.auth import authorization_required

__all__ = ["editor_blueprint"]

editor_blueprint = Blueprint("editor", __name__, url_prefix="/editor")


@editor_blueprint.route("", methods=["POST"])
@authorization_required
def create_editor():
    res = EditorUseCase().create_editor(
        CreateEditorRequest(
            **request.get_json(), user_id=session["user_info"]["user_id"]
        )
    )

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND

    session["rooms"] = session.get("rooms", {})
    session["rooms"][res.access_token] = {
        "name": res.name,
        "language": res.language,
        "token": res.access_token,
        "max_connections": res.max_connections,
        "owner_id": session["user_info"]["user_id"],
    }

    return jsonify(
        {
            "message": "Editor Created",
            "data": res.to_json(),
            "room": session["rooms"][res.access_token],
        }
    )


@editor_blueprint.route("/<editor_id>", methods=["PUT"])
@authorization_required
def edit_editor(editor_id: int):
    res = EditorUseCase().edit_editor(
        EditEditorRequest(
            **request.get_json(),
            editor_id=editor_id,
            owner_id=session["user_info"]["user_id"]
        )
    )

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND
    return jsonify({"message": "OK", "data": res.to_json()})


@editor_blueprint.route("/<editor_id>", methods=["DELETE"])
@authorization_required
def delete_editor(editor_id: int):
    res = EditorUseCase().delete_editor(DeleteEditorRequest(editor_id=editor_id))

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND
    return jsonify({"message": "OK", "data": None})


@editor_blueprint.route("/<user_id>/room", methods=["GET"])
@authorization_required
def list_editors(user_id: int):
    res = EditorUseCase().list_editors(ListEditorRequest(user_id=user_id))

    return jsonify({"message": "OK", "data": [editor.to_json() for editor in res]})


@editor_blueprint.route("/<token_access>", methods=["GET"])
@authorization_required
def get_editor(token_access: str):
    rooms = session.get("rooms", {})
    room = rooms.get(token_access)

    if not room:
        return jsonify({"message": "Room Editor Not Found", "data": None})

    res = EditorUseCase().get_editor(GetEditorRequest(access_token=token_access))

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND
    return jsonify({"message": "OK", "data": res.to_json(), "room": room})
