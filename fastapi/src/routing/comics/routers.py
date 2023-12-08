from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.schemas.comics.schema import Ratings
from src.services.comics import service as ComicsService
from src.services.database.core import get_async_session

from src.services.database.models import (
    Ratings as RatingsModel,
    Comics as ComicsModel, update_comics_rating
)

router = APIRouter()


@router.post('/ratings', tags=['ratings'])
async def create_rating(data: Ratings, session: AsyncSession = Depends(get_async_session)):
    response = await ComicsService.create_rating(data, session)
    return response


@router.get('/comics/{id}', tags=['comics'])
async def get_comics(id: int, session: AsyncSession = Depends(get_async_session)):
    response = await ComicsService.get_comics(id, session)
    return response


@router.get('/comics/', tags=['comics'])
async def get_all(session: AsyncSession = Depends(get_async_session)):
    response = await ComicsService.get_all_comics(session)
    return response

@router.get('/comics/{id}/rating', tags=['comics'])
async def get_personal_rating(id: int, session: AsyncSession = Depends(get_async_session)):
    response = await ComicsService.get_comics_rating(id, session)
    return response
