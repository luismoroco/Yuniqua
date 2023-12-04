from typing import Dict

from .request import RunPythonScriptRequest
from src.yuniqua.services.exec import Execution, Python

__all__ = ["ExecutionUseCase"]


class ExecutionUseCase:
    python: Execution

    def __init__(self):
        self.python = Python()

    def run_python(self, request: RunPythonScriptRequest) -> Dict:
        return {"message": "OK", "data": self.python.run(request.code)}
