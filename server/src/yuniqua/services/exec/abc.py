import abc

__all__ = ["Execution"]


class Execution(abc.ABC):
    @abc.abstractmethod
    def run(self, code: str) -> str:
        raise NotImplementedError
