from loguru import logger
from todo.dao import task


async def add_task(task_data):
    try:
        name = task_data.name
        name.join("Include")
        task_data.name = name

        logger.info(task_data.name)
        return await task.create(obj_in=task_data)
    except Exception as e:
        logger.error(f"Error in add task {e}")
        raise e
