from typing import Union
from uuid import UUID

from sqlalchemy import and_, update
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import UpdateUser
from db.models import User


class UserDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, name: str, surname: str, email: str) -> User:
        new_user = User(
            name=name,
            surname=surname,
            email=email
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

    async def delete_user(self, user_id: UUID) -> Union[UUID, None]:
        query = update(User).\
            where(and_(User.user_id == user_id, User.is_active == True)).\
            values(is_active=False).\
            returning(User.user_id)
        res = await self.db_session.execute(query)
        deleted_id = res.fetchone()
        return deleted_id[0] if deleted_id else None

    async def change_user_info(self, user_id: UUID, body: UpdateUser):
        pass

