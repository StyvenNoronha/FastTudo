from uuid import UUID
from fastapi import APIRouter, Depends
from schemas.task_schema import TaskDetail, TaskCreate
from models.user_models import User
from api.dependencies.user_deps import get_current_user
from services.task_service import TaskService
from models.task_model import Task
from typing import List
task_router = APIRouter()

@task_router.get('/', summary='Lista as Tarefas', response_model=List[TaskDetail])
async def list_tasks(user: User = Depends(get_current_user)):
    return await TaskService.list_tasks(user)


@task_router.get('/{task_id}', summary='Detalhe de uma Tarefa por ID', response_model=TaskDetail)
async def detail(task_id: UUID, user: User = Depends(get_current_user)):
    return await TaskService.detail(user, task_id)


@task_router.post('/create', summary='adicona tarefa', response_model=Task)
async def create_task(data: TaskCreate, user: User = Depends(get_current_user)):
    return await TaskService.create_task(user, data)