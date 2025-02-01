from typing import Literal, overload


@overload
def func(type_: Literal["type_int"], param: int) -> None:
    ...


@overload
def func(type_: Literal["type_str"], param: str) -> None:
    ...


def func(type_: Literal["type_int", "type_str"], param: int | str) -> None:
    if type_ == "type_int":
        reveal_type(param)  # Type of "param" is "int | str"
    elif type_ == "type_str":
        reveal_type(param)  # Type of "param" is "int | str"
