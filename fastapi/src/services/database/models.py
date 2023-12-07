from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Session

from .core import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)


class Comics(Base):
    __tablename__ = 'comics'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    author = Column(String)
    rating = Column(Float, nullable=True, default=0)


class Ratings(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, index=True)
    comics_id = Column(ForeignKey('comics.id', ondelete='CASCADE'))
    comics = relationship('Comics', backref='ratings', uselist=False)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship('Users', backref='ratings', uselist=False)
    value = Column(Integer)


def update_comics_rating(instance, db: Session):
    comics = db.query(Comics).filter(Comics.id == instance.comics_id).first()
    avg_rating = db.query(func.avg(Ratings.value)).filter(Comics.id == instance.comics_id).first()[0]
    comics.rating = avg_rating
    db.commit()
    db.refresh(comics)

