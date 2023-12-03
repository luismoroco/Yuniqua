import abc

__all__ = ["TokenBase"]


class TokenBase(abc.ABC):
    @abc.abstractmethod
    def generate_token(self) -> str:
        raise NotImplementedError
