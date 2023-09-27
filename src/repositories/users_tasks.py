from models.users import Users
from models.tasks import Tasks
from utils.repository import SQLAlchemyTwoModelsRepository


class UsersTasksRepository(SQLAlchemyTwoModelsRepository):
    model_user = Users
    model_task = Tasks
