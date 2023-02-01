import asyncio
import os
from typing import Any, Generator

import asyncpg
import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

import settings
from db.connect import get_db
from main import app

test_engine = create_async_engine(
    settings.TEST_DATABASE_URL,
    future=True,
    echo=True,
)

test_async_session = sessionmaker(
    test_engine,
    expire_on_commit=False,
    class_=AsyncSession
)

CLEAN_TABLES = [
    'users',
]


@pytest.fixture(scope='session', autouse=True)
async def run_migrations():
    os.system('alembic init migrations')
    os.system('alembic revision --autogenerate -m "test running migrations"')
    os.system('alembic upgrade heads')

