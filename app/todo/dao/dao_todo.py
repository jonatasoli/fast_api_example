from ..models.models_task import Task

async def addTask(task_name):
    task = await Task.create(name=task_name.name, completed=task_name.completed)
    return task.dict()
