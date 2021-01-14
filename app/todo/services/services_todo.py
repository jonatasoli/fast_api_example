from loguru import logger
from todo.dao.dao_todo import addTask


async def add_task(task_data):
    task_data.name.join("Include")

    logger.info(task_data.name)
    return await addTask(task_data)
