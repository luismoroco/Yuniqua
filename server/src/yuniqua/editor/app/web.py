from http import HTTPStatus

from flask import Blueprint, jsonify, request, session

__all__ = ["editor_blueprint"]

editor_blueprint = Blueprint("editor", __name__, url_prefix="editor")


@editor_blueprint.route("", methods=["POST"])
def create_editor():
    pass
