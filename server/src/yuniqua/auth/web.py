from flask import Blueprint, jsonify, request
from http import HTTPStatus

from .usecase import AuthUseCase
from .request import CreateUserRequest, AuthUserCredentialsRequest

__all__ = ["auth_blueprint"]

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/", methods=["GET"])
def get_auth_app_init_route():
    return jsonify({"message": "Auth service works :v"}), HTTPStatus.OK


@auth_blueprint.route("/sign-up", methods=["POST"])
def sign_up_user_route():
    response = AuthUseCase().sign_up(CreateUserRequest(**request.get_json()))

    return jsonify(response)


@auth_blueprint.route("/log-in", methods=["POST"])
def log_in_user_route():
    response = AuthUseCase().log_in(AuthUserCredentialsRequest(**request.get_json()))

    return jsonify(response)
