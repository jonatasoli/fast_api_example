from loguru import logger
from todo.dao.dao_todo import task


async def add_task(task_data):
    name = task_data.name
    name.join("Include")
    task_data.name = name

    logger.info(task_data.name)
    return await task.create(task_name=task_data, current_user_id=task_data.current_user_id)
