from dataclasses import dataclass

__all__ = [
    "CreateUserRequest",
    "GetUserRequest",
    "DeleteUserRequest",
    "EditUserRequest",
]


@dataclass
class CreateUserRequest:
    username: str
    password: str
    alias: str


@dataclass
class GetUserRequest:
    user_id: int


@dataclass
class DeleteUserRequest:
    user_id: int


@dataclass
class EditUserRequest:
    user_id: int
    alias: str
