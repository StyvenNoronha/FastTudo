from fastapi import APIRouter

task_router = APIRouter()

@task_router.get('/test')
async def teste():
    return "Tarefas Listadas"