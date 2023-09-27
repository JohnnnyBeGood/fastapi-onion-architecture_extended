from api.tasks import router as router_tasks
from api.users import router as router_users
from api.users_tasks import router as router_users_tasks

all_routers = [router_tasks, router_users, router_users_tasks]
