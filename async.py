"""
NOTE:

The difference between Pytohn and TS is that async functions are not automatically run.
The "async/await" can be stopped in Python
"""

import asyncio


async def do_work_with_return(msg: str) -> str:
    print(f"before {msg}")
    await asyncio.sleep(1)
    print(f"after {msg}")
    return f"result: {msg}"


async def do_work(msg: str):
    print(f"before {msg}")
    await asyncio.sleep(1)
    print(f"after {msg}")


# def main_without_awaiting_with_return() -> str:
#     # do_work_with_return(msg="1")  <-- Result of async function call is not used; use "await" or assign result to variable (Pylance: reportUnusedCoroutine)
#     res = do_work_with_return(msg="1")
#     print("after do_work_with_return")
#     print(res)  <-- Don't raise an error yet, but "res" is type of "Coroutine[Any, Any, str]"
#     return res  # <-- So this will not work: Expression of type "Coroutine[Any, Any, str]" cannot be assigned to return type "str"


# def main_without_awaiting():
#     """
#     NOTE: this (sadly) works in TS
#     """
#     do_work(msg="1")  <-- Result of async function call is not used; use "await" or assign result to variable (Pylance: reportUnusedCoroutine)
#     print("after do_work")


async def main_with_await():
    """
    This is run one after the other
    """
    await do_work(msg="1")
    await do_work(msg="2")


def main_with_asyncio_run():
    """
    This is run one after the other
    """
    asyncio.run(do_work(msg="1"))
    asyncio.run(do_work(msg="2"))


def main_with_task_group():
    async def inner():
        async with asyncio.TaskGroup() as tg:
            tg.create_task(do_work(msg="1"))
            tg.create_task(do_work(msg="2"))

    asyncio.run(inner())


def main_with_task_group_with_return():
    async def inner():
        async with asyncio.TaskGroup() as tg:
            task_1 = tg.create_task(do_work_with_return(msg="1"))
            task_2 = tg.create_task(do_work_with_return(msg="2"))
        print("Result of task_1:", task_1.result())
        print("Result of task_2:", task_2.result())

    asyncio.run(inner())


if __name__ == "__main__":
    # main_without_awaiting_with_return()
    # main_without_awaiting()
    asyncio.run(main_with_await())
    # main_with_asyncio_run()
    # main_with_task_group()
    # main_with_task_group_with_return()
