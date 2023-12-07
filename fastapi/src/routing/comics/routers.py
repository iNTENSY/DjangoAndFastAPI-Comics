from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.comics.schema import Ratings
from services.comics import service as ComicsService
from services.database.core import get_db


router = APIRouter()


@router.post('/ratings', tags=['ratings'])
async def create_rating(data: Ratings, db: Session = Depends(get_db)):
    return ComicsService.create_rating(data, db)


@router.get('/comics/{id}', tags=['comics'])
async def get_comics(id: int, db: Session = Depends(get_db)):
    return ComicsService.get_comics(id, db)


@router.get('/comics/{id}/rating', tags=['comics'])
async def get_personal_rating(id: int, db: Session = Depends(get_db)):
    return ComicsService.get_comics_rating(id, db)
