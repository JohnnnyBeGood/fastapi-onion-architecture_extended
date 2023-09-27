from repositories.tasks import TasksRepository
from repositories.users import UsersRepository
from repositories.users_tasks import UsersTasksRepository
from services.tasks import TasksService
from services.users import UsersService
from services.users_tasks import UsersTasksService


def tasks_service():
    return TasksService(TasksRepository)


def users_service():
    return UsersService(UsersRepository)


def users_and_tasks_service():
    return UsersTasksService(UsersTasksRepository)
