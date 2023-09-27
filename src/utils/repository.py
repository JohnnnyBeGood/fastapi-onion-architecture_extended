from typing import Iterable

from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res


class SQLAlchemyTwoModelsRepository:

    model_user = None
    model_task = None

    async def get_full_list(self):
        from sqlalchemy.orm import aliased

        u1 = aliased(self.model_user)  # type: ignore
        u2 = aliased(self.model_user)  # type: ignore
        title = aliased(self.model_task, name="title")
        author = aliased(self.model_user, name="author")
        assignee = aliased(self.model_user, name="assignee")

        async with async_session_maker() as session:
            stmt = (
                select(
                    self.model_task.title.label("title"),
                    u1.name.label("author"),
                    u2.name.label("assignee"),
                )
                .join_from(
                    self.model_task,
                    u1,
                    u1.id == self.model_task.author_id,
                )
                .join_from(self.model_task, u2, u2.id == self.model_task.assignee_id)
            )
            result = await session.execute(stmt)
            await session.commit()
            print(stmt)
            # result: Iterable[self.model_task] = result.fetchall()
            result = [self.row_to_dict(row) for row in result]
            return result

    def row_to_dict(self, row) -> {}:
        _dict = {}
        for key in row._mapping.keys():
            _dict[key] = getattr(row, key)
        return _dict
