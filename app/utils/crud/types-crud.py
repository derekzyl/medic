from typing import Any, Generic, List, TypedDict, TypeVar

from pydantic import BaseModel

T = TypeVar('T')

class ResponseMessage(Generic[T], TypedDict):
    success_status: bool
    message: str
    error:Any
    data: T|None
    doc_length: int
