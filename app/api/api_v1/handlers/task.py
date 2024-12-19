from fastapi import APIRouter, Depends
from schemas.task_schema import TaskDetail
from models.user_models import User
from api.dependencies.user_deps import get_current_user

task_router = APIRouter()

@task_router.get('/', summary='Lista as Tarefas', response_model=TaskDetail)
async def list_tasks(user: User = Depends(get_current_user)):
    pass