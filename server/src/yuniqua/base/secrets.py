import secrets

__all__ = ["YuniquaSecrets"]


class YuniquaSecrets:
    size = 4

    def __init__(self):
        self.module = secrets
