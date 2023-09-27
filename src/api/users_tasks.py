from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import users_and_tasks_service
from schemas.tasks import TaskSchemaAdd
from services.users_tasks import UsersTasksService

router = APIRouter(
    prefix="/users-tasks-list",
    tags=["Users & Tasks"],
)


@router.get("/")
async def get_users_and_tasks(
    users_and_tasks_service: Annotated[
        UsersTasksService, Depends(users_and_tasks_service)
    ],
):
    users_tasks = await users_and_tasks_service.get_all_records()
    return users_tasks
