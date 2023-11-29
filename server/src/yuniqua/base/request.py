from typing import TypeVar
from dataclasses import dataclass

T = TypeVar("T")

__all__ = ["RequestMapper"]


@dataclass
class RequestMapper:
    def __init__(self, data: T) -> None:
        self.map_request_data(data)

    def map_request_data(self, data: T) -> None:
        for field in self.__dataclass_fields__:
            setattr(self, field, data.get(field, None))
