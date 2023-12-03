from typing import Optional
from dataclasses import dataclass

__all__ = [
    "CreateEditorRequest",
    "EditEditorRequest",
    "DeleteEditorRequest",
    "ListEditorRequest",
    "GetEditorRequest",
]


@dataclass
class CreateEditorRequest:
    user_id: int
    name: str
    max_connections: int
    language: str


@dataclass
class EditEditorRequest:
    editor_id: int
    name: Optional[str]
    max_connections: Optional[int]
    language: Optional[str]


@dataclass
class DeleteEditorRequest:
    editor_id: int


@dataclass
class ListEditorRequest:
    user_id: int


@dataclass
class GetEditorRequest:
    access_token: str
