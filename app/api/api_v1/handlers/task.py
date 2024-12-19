from uuid import UUID
from fastapi import APIRouter, Depends
from schemas.task_schema import TaskDetail, TaskCreate, TaskUpdate
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

'''
Tem algum erro na taskcreate
@task_router.post('/create', summary='adicona tarefa', response_model=Task)
async def create_task(data: TaskCreate, user: User = Depends(get_current_user)):
    return await TaskService.create_task(user, data)

'''
@task_router.put('/{task_id}', summary='Atualiza Tarefa', response_model=TaskDetail)
async def update(task_id: UUID, data: TaskUpdate, user: User = Depends(get_current_user)):
    return await TaskService.update_task(user, task_id, data)

@task_router.delete('/{task_id}', summary='Exclui Tarefa')
async def delete(task_id: UUID, user: User = Depends(get_current_user)):
    await TaskService.delete_task(user, task_id)
    return None

