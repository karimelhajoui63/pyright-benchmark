# AFAIK, this only can be done through @overload
# Otherwise, the `func` cannot be "run/resolved" by the static type checker
# This example is trivial, but it can be way more complex, so the type checker just check the returned type hint

from typing import Literal, overload


@overload
def func(x: Literal["str"]) -> str:
    ...


@overload
def func(x: Literal["int"]) -> int:
    ...


def func(x: Literal["str", "int"]) -> int | str:
    if x == "str":
        return ""
    elif x == "int":
        return 1


# 😕: the "str" isn't proposed on the IDE. Only the last one ("int") is proposed.
res = func("str")
# reveal_type(res)  <-- Type of "res" is "str" (Pylance)
res = func("int")
# reveal_type(res)  <-- Type of "res" is "str" (Pylance)
