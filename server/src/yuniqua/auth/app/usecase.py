from typing import Dict, Union

from src.yuniqua.user.repository import UserRepository, UserPostgresRepository
from src.yuniqua.database.model import YuniquaUser
from src.yuniqua.services.crypt import BcryptService
from .request import LogInRequest

__all__ = ["AuthUseCase"]


class AuthUseCase:
    user_repository: UserRepository

    def __init__(self):
        self.user_repository = UserPostgresRepository()
        self.bcrypt_service = BcryptService()

    def log_in(self, request: LogInRequest) -> Union[YuniquaUser, Dict]:
        user = self.user_repository.get_user(username=request.username)

        if not user:
            return {"message": "User Not Found", "data": None}

        password_valid = self.bcrypt_service.verify(
            hash=user.password, plain_text=request.password
        )

        if not password_valid:
            return {"message": "Bad credentials", "data": None}

        return user
