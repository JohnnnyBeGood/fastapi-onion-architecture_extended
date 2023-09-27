from pydantic import BaseModel


class UsersTasksSchemaInDB(BaseModel):
    title: str
    author: str
    assignee: str
