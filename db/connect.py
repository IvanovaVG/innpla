from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

import settings

engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)  # echo - logging for db

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
