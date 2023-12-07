from fastapi import Depends
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from schemas.comics.schema import Ratings, Comics
from services.database.core import get_db, get_or_create
from services.database.models import Ratings as RatingsModel, Comics as ComicsModel, update_comics_rating


def create_rating(data: Ratings, db: Session):
    if not (1 <= data.value <= 5):
        return {'error': 'Value can be from 1 to 5.'}

    try:
        obj = db.query(RatingsModel).filter(
            RatingsModel.user_id == data.user_id, RatingsModel.comics_id == data.comics_id
        ).first()
        obj.value = data.value
    except Exception as ex:
        obj = RatingsModel(comics_id=data.comics_id, user_id=data.user_id, value=data.value)
        db.add(obj)

    db.commit()
    db.refresh(obj)

    update_comics_rating(obj, db)

    return obj


def get_comics(id: int, db: Session):
    try:
        obj = db.query(ComicsModel).filter(ComicsModel.id == id).first()
    except NoResultFound:
        return {'error': 'object not found'}

    return obj