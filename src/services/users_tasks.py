from schemas.tasks import TaskSchema
from schemas.users import UserSchema

from utils.repository import SQLAlchemyTwoModelsRepository


class UsersTasksService:
    def __init__(self, new_repo: SQLAlchemyTwoModelsRepository):
        self._new_repo: SQLAlchemyTwoModelsRepository = new_repo()

    async def get_all_records(self):
        users_and_tasks = await self._new_repo.get_full_list()
        return users_and_tasks
