from datetime import date
from typing import Iterable

from sqlalchemy.orm import Session

from . import models
from . import schemas


def get_article(db: Session, article_id: str) -> models.Article:
    return db.query(models.Article).filter(models.Article.id == article_id).first()


def get_articles_by_publication_date(
    db: Session, article_date: date
) -> Iterable[models.Article]:
    return (
        db.query(models.Article)
        .filter(models.Article.publication_date == article_date)
        .all()
    )


def get_articles(
    db: Session, skip: int = 0, limit: int = 100
) -> Iterable[models.Article]:
    return db.query(models.Article).offset(skip).limit(limit).all()


def create_article(db: Session, article: schemas.ArticleCreate) -> models.Article:
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def update_article(db: Session, article: schemas.ArticleUpdate) -> models.Article:
    new_article = models.Article(**article.dict())
    old_article = get_article(db, new_article.id)
    db.delete(old_article)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    pass


def get_user(db: Session, user_id: int) -> models.User:
    pass


def get_user_by_email(db: Session, email: str) -> models.User:
    pass


def get_users(db: Session, skip: int = 0, limit: int = 100) -> Iterable[models.User]:
    pass


def create_user_rating(
    db: Session, user_rating: schemas.UserRatingCreate, article_id: int, user_id: int
) -> models.UserRating:
    pass


def get_user_rating(db: Session, user_rating_id: int) -> models.UserRating:
    pass


def get_user_ratings_by_user(db: Session, user_id: int) -> Iterable[models.UserRating]:
    pass


def get_user_ratings_by_article(
    db: Session, article_id: int
) -> Iterable[models.UserRating]:
    pass


def get_user_ratings(
    db: Session, skip: int = 0, limit: int = 100
) -> Iterable[models.UserRating]:
    pass
