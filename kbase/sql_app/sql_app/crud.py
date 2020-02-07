from datetime import date
from typing import Iterable

from passlib.handlers.sha2_crypt import sha512_crypt
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


def get_hash(text: str) -> str:
    hashed_text = sha512_crypt.encrypt(text, rounds=114241)
    return hashed_text


def verify_hash(hashed: str, plain: str) -> bool:
    return sha512_crypt.verify(hashed, plain)


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = get_hash(user.password)
    db_user = models.User(
        email=user.email, name=user.name, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> Iterable[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user_rating(
    db: Session, user_rating: schemas.UserRatingCreate, article_id: str, user_id: int
) -> models.UserRating:
    db_user_rating = models.UserRating(
        user_id=user_id, article_id=article_id, value=user_rating.value
    )
    db.add(db_user_rating)
    db.commit()
    db.refresh(db_user_rating)
    return db_user_rating


def get_user_rating(db: Session, user_rating_id: int) -> models.UserRating:
    return (
        db.query(models.UserRating)
        .filter(models.UserRating.id == user_rating_id)
        .first()
    )


def get_user_ratings_by_user(db: Session, user_id: int) -> Iterable[models.UserRating]:
    return (
        db.query(models.UserRating).filter(models.UserRating.user_id == user_id).all()
    )


def get_user_ratings_by_article(
    db: Session, article_id: int
) -> Iterable[models.UserRating]:
    return (
        db.query(models.UserRating)
        .filter(models.UserRating.article_id == article_id)
        .all()
    )


def get_user_ratings(
    db: Session, skip: int = 0, limit: int = 100
) -> Iterable[models.UserRating]:
    return db.query(models.UserRating).offset(skip).limit(limit).all()
