from http import HTTPStatus

from flask import Blueprint, jsonify, request

from src.yuniqua.base.auth import authorization_required
from .usecase import ExecutionUseCase
from .request import RunPythonScriptRequest

__all__ = ["execution_blueprint"]


execution_blueprint = Blueprint("execute", __name__, url_prefix="/execute")


@execution_blueprint.route("/python", methods=["POST"])
# @authorization_required
def execute_python():
    res = ExecutionUseCase().run_python(RunPythonScriptRequest(**request.get_json()))

    return jsonify(res), HTTPStatus.OK
