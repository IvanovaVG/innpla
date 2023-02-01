from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import CreateUser, ShowUser
from db.connect import get_db
from db.crud import UserDAL

user_router = APIRouter()


async def _create_user(body: CreateUser, db: AsyncSession) -> ShowUser:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name,
                surname=body.surname,
                email=body.email
            )
            return ShowUser(
                user_id=user.user_id,
                name=user.name,
                surname=user.surname,
                email=user.email,
                is_active=user.is_active
            )


@user_router.post('/', response_model=ShowUser)
async def create_user(body: CreateUser, db: AsyncSession = Depends(get_db)) -> ShowUser:
    return await _create_user(body=body, db=db)
