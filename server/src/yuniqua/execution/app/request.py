from dataclasses import dataclass

__all__ = ["RunPythonScriptRequest"]


@dataclass
class RunPythonScriptRequest:
    code: str
