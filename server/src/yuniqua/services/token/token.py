from .abc import TokenBase
from src.yuniqua.base.secrets import YuniquaSecrets

__all__ = ["TokenService"]


class TokenService(YuniquaSecrets, TokenBase):
    def __init__(self):
        super().__init__()

    def generate_token(self) -> str:
        return self.module.token_hex(self.size)
