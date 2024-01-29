# Advantages to use wraps:
# https://hayageek.com/functools-wraps-in-python/#:~:text=In%20Python%2C%20the%20module%20functools,without%20permanently%20modifying%20their%20behavior.
# (it works without, but it's better with)
from functools import wraps
from typing import Callable, Concatenate


def add_logging[T, **P](f: Callable[P, T]) -> Callable[P, T]:
    """A type-safe decorator to add logging to a function."""

    @wraps(f)
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"{f.__name__} was called")
        return f(*args, **kwargs)

    return inner


def add_logging_with_msg(msg: str):
    def add_logging[T, **P](f: Callable[P, T]) -> Callable[P, T]:
        """A type-safe decorator to add logging to a function."""

        @wraps(f)
        def inner(*args: P.args, **kwargs: P.kwargs) -> T:
            print(f"{msg} {f.__name__} was called")
            return f(*args, **kwargs)

        return inner

    return add_logging


def add_logging_with_added_params[T, **P](
    f: Callable[P, T],
) -> Callable[Concatenate[str, P], T]:
    """A type-safe decorator to add logging to a function."""

    @wraps(f)
    def inner(msg: str, *args: P.args, **kwargs: P.kwargs) -> T:
        print(f"{msg}: {f.__name__} was called")
        return f(*args, **kwargs)

    return inner


# ------------------------


@add_logging
def func_w_simple_decorator(x: float, y: float) -> float:
    """Add two numbers together."""
    return x + y


@add_logging_with_msg(msg="LOGGING:")
def func_w_decorator_w_params(x: float, y: float) -> float:
    """Add two numbers together."""
    return x + y


@add_logging_with_added_params
def func_w_decorator_that_add_params(x: float, y: float) -> float:
    """Add two numbers together."""
    return x + y


# ------------------------


res = func_w_simple_decorator(1, 2)  # func_w_simple_decorator was called
# reveal_type(res)  <-- Type of "res" is "float" (Pylance)

res = func_w_decorator_w_params(1, 2)  # LOGGING: func_w_decorator_w_params was called
# reveal_type(res)  <-- Type of "res" is "float" (Pylance)

# 😕: ParamSpec does not support concatenating keyword arguments as of now. Only positional-only arguments can be added. – PIG208 Mar 30, 2023 at 19:14
# here: https://stackoverflow.com/q/75890433
res = func_w_decorator_that_add_params("LOGGING", 1, 2)
# reveal_type(res)  <-- Type of "res" is "float" (Pylance)
