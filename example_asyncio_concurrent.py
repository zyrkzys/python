import asyncio

async def my_task1():
    print("Running task 1")
    await asyncio.sleep(1)
    print("Task 1 complete")

async def my_task2():
    print("Running task 2")
    await asyncio.sleep(1)
    print("Task 2 complete")

loop = asyncio.get_event_loop()
tasks = [my_task1(), my_task2()]
loop.run_until_complete(asyncio.gather(*tasks))
