from fastapi import HTTPException, Depends
from sqlalchemy import select, insert
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.schemas.comics.schema import Ratings, Comics
from src.services.database.core import get_async_session
from src.services.database.models import (
    Ratings as RatingsModel,
    Comics as ComicsModel, update_comics_rating
)


async def create_rating(data: Ratings, session: AsyncSession):
    if not (1 <= data.value <= 5):
        return {'error': 'Value can be from 1 to 5.'}

    try:
        query = select(RatingsModel).where(RatingsModel.user_id == data.user_id, RatingsModel.comics_id == data.comics_id)
        result = await session.execute(query)
        obj = result.first()[0]
        obj.value = data.value
    except (Exception, NoResultFound):
        query = insert(RatingsModel).values(comics_id=data.comics_id,
                                            user_id=data.user_id,
                                            value=data.value)
        result = await session.execute(query)
        obj = result.scalar_one()
        print(obj)
    finally:
        await session.commit()
    await update_comics_rating(obj, session)
    return obj


async def get_comics(id: int, session: AsyncSession):
    try:
        query = select(ComicsModel).where(ComicsModel.id == id)
        result = await session.execute(query)
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'error'
        })
    return result.scalars().all()


async def get_all_comics(session: AsyncSession):
    try:
        query = select(ComicsModel)
        result = await session.execute(query)
    except Exception:
        raise HTTPException(status_code=500)

    return result.scalars().all()


async def get_comics_rating(id: int, session: AsyncSession):
    try:
        query = select(ComicsModel).where(ComicsModel.id == id)
        result = await session.execute(query)
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'error'
        })
    return {'value': result.first()[0].rating}
