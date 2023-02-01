from typing import Union
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import (
    CreateUser,
    DeletedUser,
    ShowUser,
    UpdatedUser,
    UpdateUser
)
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


async def _delete_user(user_id: UUID, db: AsyncSession) -> Union[UUID, None]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            deleted_id = await user_dal.delete_user(user_id=user_id)
            return deleted_id


async def _change_user_info(user_id: UUID, update_user_info: dict, db: AsyncSession) -> Union[UUID, None]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            changed_user = await user_dal.change_user_info(user_id=user_id, **update_user_info)
            return changed_user


async def _get_user_by_id(user_id: UUID, db: AsyncSession) -> Union[ShowUser, None]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.get_user_by_id(user_id=user_id)
            return ShowUser(
                user_id=user.user_id,
                name=user.name,
                surname=user.surname,
                email=user.email,
                is_active=user.is_active
            ) if user else user


@user_router.post('/', response_model=ShowUser)
async def create_user(body: CreateUser, db: AsyncSession = Depends(get_db)) -> ShowUser:
    return await _create_user(body=body, db=db)


@user_router.delete('/', response_model=DeletedUser)
async def delete_user(user_id: UUID, db: AsyncSession = Depends(get_db)) -> DeletedUser:
    deleted_user_id = await _delete_user(user_id=user_id, db=db)
    if not deleted_user_id:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not found')
    return DeletedUser(deleted_id=deleted_user_id)


@user_router.patch('/', response_model=UpdatedUser)
async def change_user_info(user_id: UUID, body: UpdateUser, db: AsyncSession = Depends(get_db)) -> UpdatedUser:
    update_user_info = body.dict(exclude_none=True)
    if update_user_info == {}:
        raise HTTPException(status_code=422, detail='Info for change is empty')
    user_in_db = await _get_user_by_id(user_id=user_id, db=db)
    if not user_in_db:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not found')
    change_user = await _change_user_info(user_id=user_id, update_user_info=update_user_info, db=db)
    return UpdatedUser(updated_id=change_user)





