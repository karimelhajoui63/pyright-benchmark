# -----------------------------------------------------------------------------
# Enum
# -----------------------------------------------------------------------------

from enum import Enum


class Status(Enum):
    READY = "ready"
    GO = "go"


def func_enum(status: Status):
    print(f"{status=}")


def test_enum(status: str):
    if status in Status:
        print("✅")
    else:
        print("❌")


func_enum(status=Status.READY)
# func_enum(status="ready")  <-- Argument of type "Literal['ready']" cannot be assigned to parameter "status" of type "Status" in function "func_enum"

test_enum(status="READY")  # ❌
test_enum(status="ready")  # ✅
# test_enum(status=Status.READY)  <-- Argument of type "Literal[Status.READY]" cannot be assigned to parameter "status" of type "str" in function "test_literal"


# -----------------------------------------------------------------------------
# Literal
# -----------------------------------------------------------------------------

from typing import Literal

STATUS = Literal["READY", "GO"]


def func_literal(status: STATUS):
    print(f"{status=}")


# def test_literal(status: str):
#     if status in STATUS:  <-- Operator "in" not supported for types "str" and "STATUS"
#         return True
#     return False

func_literal("READY")  # <-- autocompletion (like in TS)
func_literal("GO")
# func_literal("READDY")  <-- Argument of type "Literal['READDY']" cannot be assigned to parameter "status" of type "STATUS" in function "func"
