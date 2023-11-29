import abc

__all__ = ["CryptBase"]


class CryptBase(abc.ABC):
    @abc.abstractmethod
    def encrypt(self, **kwargs) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def verify(self, **kwargs) -> bool:
        raise NotImplementedError
