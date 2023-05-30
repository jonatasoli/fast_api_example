from loguru import logger

from todo.unit_of_work import AbstractUnitOfWork



async def add_task(task_data, uow = AbstractUnitOfWork):
    async with uow:
        task = uow.todo.add(task_data)
        await uow.commit()
    return await task 


async def update_task(task_id, task_data, uow = AbstractUnitOfWork):
    async with uow:
        task = await uow.todo.update_task(task_id, task_data)
        await uow.commit()
    return task 


async def get_task(task_id, uow = AbstractUnitOfWork):
    async with uow:
        task = await uow.todo.get(task_id)
        await uow.commit()
    return task
