import uvicorn
import asyncio
from fastapi import FastAPI
from db.db import init_db

from api.routers import all_routers


app = FastAPI(title="Упрощенный аналог Jira/Asana с дополнением")


for router in all_routers:
    app.include_router(router)


if __name__ == "__main__":
    asyncio.run(init_db())
    uvicorn.run(app="main:app", reload=True)
