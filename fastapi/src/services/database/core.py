from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import DB_USER, DB_HOST, DB_PORT, DB_PASS, DB_NAME


SQLALCHEMY_DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


async def get_async_session():
    async with async_session_maker() as session:
        yield session
