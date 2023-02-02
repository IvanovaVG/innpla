import re
import uuid
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, constr, validator

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class Config:
        orm_mode = True  # all objects to json only for return to user


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool


class DeletedUser(BaseModel):
    deleted_id: uuid.UUID


class UpdatedUser(BaseModel):
    updated_id: uuid.UUID


class UpdateUser(TunedModel):
    name: Optional[constr(min_length=1)]
    surname: Optional[constr(min_length=1)]
    email: Optional[EmailStr]

    @validator('name')
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail='Name should contains only letters')
        return value

    @validator('surname')
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail='Surname should contains only letters')
        return value


class AuthCodeResponse(TunedModel):
    user_id: uuid.UUID
    code: int


class CreateUser(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str

    @validator('name')
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail='Name should contains only letters')
        return value

    @validator('surname')
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail='Surname should contains only letters')
        return value
