from typing import Any, Dict, Mapping, Type, TypeVar

from pymongo.collection import Collection
from typing_extensions import TypedDict

from mongoengine.base import BaseDocument
from mongoengine.queryset.queryset import QuerySet

_U = TypeVar("_U", bound="Document")

_MetaDict = Mapping[str, Any]

class _UnderMetaDict(TypedDict):
    strict: bool
    collection: str

class Document(BaseDocument):
    meta: _MetaDict
    _meta: _UnderMetaDict
    _fields: Dict[str, Any]
    _collection: Collection[Any] | None

    @classmethod
    def objects(cls: Type[_U]) -> QuerySet[_U]:
        """
        from:
        https://github.com/python/peps/blob/50a31d14b467aba0cc0168408369d2bb28e9b4e2/pep-0484.txt#L1260-L1270
        """
        ...

    def save(
        self: _U,
        force_insert: bool = ...,
        validate: bool = ...,
        clean: bool = ...,
        write_concern: Any = ...,
        cascade: Any = ...,
        cascade_kwargs: Any = ...,
        _refs: Any = ...,
        save_condition: Any = ...,
        signal_kwargs: Any = ...,
    ) -> _U: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
