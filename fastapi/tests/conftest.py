import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app import app
from config import DB_NAME_TEST, DB_PORT_TEST, DB_PASS_TEST, DB_USER_TEST, DB_HOST_TEST
from services.database.core import Base, get_async_session

SQLALCHEMY_DATABASE_URL = f'postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}'
engine_test = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal_test = sessionmaker(autoflush=False, autocommit=False, bind=engine_test)
Base.bind = engine_test


def override_get_async_session():
    db = SessionLocal_test()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.fixture(autouse=True, scope='session')
def prepare_database():
    with engine_test.begin() as conn:
        conn.run_sync(Base.create_all())
    yield
    with engine_test.begin() as conn:
        conn.run_sync(Base.drop_all())


client = TestClient(app, base_url='http:/localhost')

