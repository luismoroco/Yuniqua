import sys
from io import StringIO

from src.yuniqua.services.exec.abc import Execution

__all__ = ["Python"]


class Python(Execution):
    def run(self, script: str) -> str:
        stdout = sys.stdout
        buffer = StringIO()
        sys.stdout = buffer

        try:
            exec(script)
            return buffer.getvalue()
        except Exception as e:
            return f"Error:\n{str(e)}"
        finally:
            sys.stdout = stdout
