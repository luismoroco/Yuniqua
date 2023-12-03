from http import HTTPStatus

from flask import Blueprint, jsonify, request, session

from .usecase import AuthUseCase
from .request import LogInRequest

__all__ = ["auth_blueprint"]

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/log-in", methods=["POST", "GET"])
def log_in():
    res = AuthUseCase().log_in(LogInRequest(**request.get_json()))

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND

    session["user_info"] = res.to_json()
    return jsonify({"message": "Logged", "data": session["user_info"]}), HTTPStatus.OK


@auth_blueprint.route("/log-out", methods=["GET"])
def log_out():
    session.pop("user_info", None)
    return {"message": "OK", "data": None}
