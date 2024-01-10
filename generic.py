def first[T](items: list[T]) -> T:  # Function is generic over the TypeVar "T"
    return items[0]


res = first(items=[1, 2])
# reveal_type(res)  <-- Type of "res" is "int" (Pylance)
