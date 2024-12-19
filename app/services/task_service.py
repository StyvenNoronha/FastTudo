from uuid import UUID
from models.user_models import User
from models.task_model import Task
from typing import List
from schemas.task_schema import TaskCreate

class TaskService:
    @staticmethod
    async def list_tasks(user: User) -> List[Task]:
        tasks = await Task.find(Task.owner.id == user.id).to_list()
        return tasks

    @staticmethod
    async def create_task(user: User, data: TaskCreate) -> Task:
        task = Task(**data.dict(), owner=user)
        return await task.insert()
    

    @staticmethod
    async def detail(user: User, task_id: UUID):
        task = await Task.find_one(Task.task_id == task_id, Task.owner.id == user.id)
        return task    