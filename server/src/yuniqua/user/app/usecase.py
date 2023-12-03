from typing import Dict, Union
from datetime import datetime

from src.yuniqua.database.db import session
from src.yuniqua.database.model import YuniquaUser
from src.yuniqua.user.repository import UserRepository, UserPostgresRepository
from src.yuniqua.services.crypt import BcryptService
from .request import (
    CreateUserRequest,
    GetUserRequest,
    DeleteUserRequest,
    EditUserRequest,
)

__all__ = ["UserUseCase"]


class UserUseCase:
    repository: UserRepository
    bcrypt_service: "BcryptService"

    def __init__(self):
        self.repository = UserPostgresRepository()
        self.bcrypt_service = BcryptService()

    def create_user(self, request: CreateUserRequest) -> Union[Dict, YuniquaUser]:
        user = self.repository.get_user(username=request.username)

        if user:
            return {"message": "User already exist", "data": None}

        pass_hash = self.bcrypt_service.encrypt(plain_text=request.password)

        user = YuniquaUser()
        user.username = request.username
        user.password = pass_hash
        user.alias = request.alias
        user.created_at = datetime.now()

        session.add(user)
        session.commit()

        return user

    def get_user(self, request: GetUserRequest) -> Union[Dict, YuniquaUser]:
        user = self.repository.get_user(user_id=request.user_id)

        if not user:
            return {"message": "User not exist", "data": None}

        return user

    def delete_user(self, request: DeleteUserRequest) -> Dict:
        user = self.repository.get_user(user_id=request.user_id)

        if not user:
            return {"message": "User not found"}

        self.repository.delete_user(user_id=request.user_id)
        session.commit()

        return {"message": "OK"}

    def edit_user(self, request: EditUserRequest) -> Union[Dict, YuniquaUser]:
        user = self.repository.get_user(user_id=request.user_id)

        if not user:
            return {"message": "User not found"}

        if request.alias:
            user.alias = request.alias

        session.add(user)
        session.commit()

        return user
