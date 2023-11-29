from typing import Dict

from flask import session

from src.yuniqua.user.repository import UserRepository, UserPostgresRepository
from src.yuniqua.services.crypt import BcryptService
from .request import CreateUserRequest, AuthUserCredentialsRequest

__all__ = ["AuthUseCase"]


class AuthUseCase:
    user_repository: UserRepository

    def __init__(self):
        self.user_repository = UserPostgresRepository()
        self.bcrypt_service = BcryptService()

    def sign_up(self, request: CreateUserRequest) -> Dict:
        user = self.user_repository.get_user(username=request.username)

        if user:
            return {"message": "User already exist"}

        hashed_password = self.bcrypt_service.encrypt(plain_text=request.password)
        user = self.user_repository.create_user(
            username=request.username, password=hashed_password
        )

        session["user_id"] = user.editor_user_id

        return {"message": "Created", "data": user.to_json()}

    def log_in(self, request: AuthUserCredentialsRequest) -> Dict:
        user = self.user_repository.get_user(username=request.username)

        if not user:
            return {"message": "User Not Found"}

        password_valid = self.bcrypt_service.verify(
            hash=user.password, plain_text=request.password
        )

        if not password_valid:
            return {"message": "Bad credentials"}

        session["user_id"] = user.editor_user_id

        return {"message": "Welcome!", "data": user.to_json()}
