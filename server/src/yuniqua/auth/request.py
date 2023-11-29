from dataclasses import dataclass

__all__ = ["CreateUserRequest", "AuthUserCredentialsRequest"]


@dataclass
class CreateUserRequest:
    username: str
    password: str


@dataclass
class AuthUserCredentialsRequest:
    username: str
    password: str
