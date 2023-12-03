from dataclasses import dataclass

__all__ = ["CreateUserRequest", "LogInRequest"]


@dataclass
class CreateUserRequest:
    username: str
    password: str


@dataclass
class LogInRequest:
    username: str
    password: str
