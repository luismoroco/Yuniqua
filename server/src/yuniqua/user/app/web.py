from http import HTTPStatus

from flask import Blueprint, jsonify, request

from src.yuniqua.user.app.request import (
    CreateUserRequest,
    GetUserRequest,
    DeleteUserRequest,
    EditUserRequest,
)
from src.yuniqua.user.app.usecase import UserUseCase


__all__ = ["user_blueprint"]

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("", methods=["POST"])
def create_user():
    res = UserUseCase().create_user(CreateUserRequest(**request.get_json()))

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.CONFLICT
    return jsonify({"message": "OK", "data": res.to_json()}), HTTPStatus.CREATED


@user_blueprint.route("/<user_id>", methods=["GET"])
def get_user(user_id: int):
    res = UserUseCase().get_user(GetUserRequest(user_id=user_id))

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND
    return jsonify({"message": "OK", "data": res.to_json()}), HTTPStatus.OK


@user_blueprint.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    res = UserUseCase().delete_user(DeleteUserRequest(user_id=user_id))

    return (
        jsonify(res),
        HTTPStatus.OK if res.get("message") == "OK" else HTTPStatus.NOT_FOUND,
    )


@user_blueprint.route("/<user_id>", methods=["PUT"])
def edit_user(user_id: int):
    res = UserUseCase().edit_user(
        EditUserRequest(**request.get_json(), user_id=user_id)
    )

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND
    return jsonify({"message": "OK", "data": res.to_json()}), HTTPStatus.OK
