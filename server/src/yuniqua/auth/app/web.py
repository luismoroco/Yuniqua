from http import HTTPStatus

from flask import Blueprint, jsonify, request, session

from src.yuniqua.base.auth import authorization_required
from .usecase import AuthUseCase
from .request import LogInRequest

__all__ = ["auth_blueprint"]

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/test", methods=["GET"])
def check_session_works():
    if "user_info" in session:
        return jsonify({"message": "Welcome", "data": session["user_info"]})
    return jsonify({"message": "User Not Found", "data": None})


@auth_blueprint.route("/log-in", methods=["POST"])
def log_in():
    res = AuthUseCase().log_in(LogInRequest(**request.get_json()))

    if isinstance(res, dict):
        return jsonify(res), HTTPStatus.NOT_FOUND

    session["user_info"] = res.to_json()
    return jsonify({"message": "Logged", "data": session["user_info"]}), HTTPStatus.OK


@auth_blueprint.route("/log-out", methods=["GET"])
@authorization_required
def log_out():
    session.pop("user_info", None)
    return {"message": "OK", "data": None}
