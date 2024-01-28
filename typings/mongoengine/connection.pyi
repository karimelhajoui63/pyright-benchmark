from typing import Any

from mongomock import MongoClient
from pymongo import ReadPreference

def connect(
    db: str | None = ...,
    alias: str | None = ...,
    name: str | None = ...,
    host: str | None = ...,
    port: str | None = ...,
    read_preference: ReadPreference = ...,
    username: str | None = ...,
    password: str | None = ...,
    authentication_source: str | None = ...,
    authentication_mechanism: str | None = ...,
    **kwargs: Any,
) -> MongoClient[Any]: ...
