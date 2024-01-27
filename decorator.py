# Advantages to use wraps:
# https://hayageek.com/functools-wraps-in-python/#:~:text=In%20Python%2C%20the%20module%20functools,without%20permanently%20modifying%20their%20behavior.
# (it works without, but it's better with)
from functools import wraps
from typing import Callable


def add_logging[T, **P](f: Callable[P, T]) -> Callable[P, T]:
    """A type-safe decorator to add logging to a function."""

    @wraps(f)
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"{f.__name__} was called")
        return f(*args, **kwargs)

    return inner


def add_logging_with_added_params():
    TODO


def add_logging_with_msg(msg: str):
    def add_logging[T, **P](f: Callable[P, T]) -> Callable[P, T]:
        """A type-safe decorator to add logging to a function."""

        @wraps(f)
        def inner(*args: P.args, **kwargs: P.kwargs) -> T:
            print(f"{msg} {f.__name__} was called")
            return f(*args, **kwargs)

        return inner

    return add_logging


@add_logging
def add_two(x: float, y: float) -> float:
    """Add two numbers together."""
    return x + y


@add_logging_with_msg(msg="LOGGING:")
def add_three(x: float, y: float, z: float) -> float:
    """Add three numbers together."""
    return x + y + z


res = add_two(1, 2)  # add_two was called
# reveal_type(res)  <-- Type of "res" is "float" (Pylance)

res = add_three(1, 2, 3)  # LOGGING: add_three was called
# reveal_type(res)  <-- Type of "res" is "float" (Pylance)
