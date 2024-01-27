from typing import NamedTuple, NotRequired, Protocol, TypedDict

from attrs import define
from pydantic import BaseModel


# attrs is type-safe ✅ (at least, at "compile" time, on the run-time, it's opt-in)
@define
class PayloadAttrs:
    id: int
    name: str = "Karim"


def func_attrs(payload: PayloadAttrs) -> int:
    # payload.name = 1  "Literal[1]" is incompatible with "str"
    return payload.id + len(payload.name)


func_attrs(payload=PayloadAttrs(id=1))


# -----------------------------------


# Pydantic is type-safe ✅ (you have to opt-out the validation part at run-time)
class PayloadPydantic(BaseModel):
    id: int
    name: str = "Karim"


def func_pydantic(payload: PayloadPydantic) -> int:
    return payload.id + len(payload.name)


func_pydantic(payload=PayloadPydantic(id=1))


# -----------------------------------


# TypedDict is type-safe ✅ (but equivalent to a simple edict at run-time)
# TypedDict classes can contain only type annotations (so: no default values)
class PayloadTypedDict(TypedDict):
    id: int
    name: NotRequired[str]


def func_typed_dict(payload: PayloadTypedDict) -> int:
    # auto-completion for the keys + warning on wrong keys ✨
    return payload["id"] + len(payload.get("name", ""))


# auto-completion for the keys + warning on wrong keys (AND value type) ✨
func_typed_dict(payload={"id": 1, "name": "Karim"})

# This way of using TypedDict is also type-safe, but there is not auto-completion (strangely)
# (*args: Any, **kwargs: Any) on the IDE
payload_type_dict = PayloadTypedDict(id=1, name="Karim")
# reveal_type(payload_type_dict)  <-- Type of "payload_type_dict" is "PayloadTypedDict"
# type(payload_type_dict)  <-- <class 'dict'>
func_typed_dict(payload=payload_type_dict)


# -----------------------------------


# NamedTuple is type-safe ✅
class PayloadNamedTuple(NamedTuple):
    id: int
    name: str = "Karim"


def func_named_tuple(payload: PayloadNamedTuple) -> int:
    # auto-completion for the keys + warning on wrong keys ✨
    return payload.id + len(payload.name)


# func_named_tuple(payload=(1, "Karim"))  <-- doesn't work

# This way of using TypedDict is also type-safe, but there is not auto-completion (strangely)
# (*args: Any, **kwargs: Any) on the IDE
payload_named_tuple = PayloadNamedTuple(id=1)
# reveal_type(payload_named_tuple)  <-- Type of "payload_named_tuple" is "PayloadNamedTuple"
# type(payload_named_tuple)  <-- <class '__main__.PayloadNamedTuple'>
func_named_tuple(payload=payload_named_tuple)

# -----------------------------------


# Protocol is type-safe ✅ but it doesn't work here ❌
# it's not made fro this use case
class PayloadProtocol(Protocol):
    id: int
    name: str = "Karim"


def func_protocal(payload: PayloadProtocol) -> int:
    # auto-completion for the keys + warning on wrong keys ✨
    return payload.id + len(payload.name)


# func_protocal(payload=NeedSomethingHere(1, ""))
