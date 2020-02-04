from datetime import date, datetime
from typing import List

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import ARRAY

from .database import SqlAlchemyBase


class Article(SqlAlchemyBase):
    __tablename__ = "articles"

    id: str = sa.Column(sa.String, primary_key=True, index=True)
    version: str = sa.Column(sa.String)
    source: str = sa.Column(sa.String)
    journal: str = sa.Column(sa.String)
    article_type: str = sa.Column(sa.String)
    title: str = sa.Column(sa.String)
    publication_date: date = sa.Column(sa.Date, index=True)
    update_date: date = sa.Column(sa.Date, index=True)
    link: str = sa.Column(sa.String)
    doid: str = sa.Column(sa.String)
    summary: str = sa.Column(sa.String)
    authors: List[str] = sa.Column(ARRAY(sa.String, dimensions=1))
    affiliations: List[str] = sa.Column(ARRAY(sa.String, dimensions=1))
    language: str = sa.Column(sa.String)
    keywords: List[str] = sa.Column(ARRAY(sa.String, dimensions=1))
    references: List[str] = sa.Column(ARRAY(sa.String, dimensions=1))


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    email = sa.Column(sa.String, unique=True, index=True)
    name = sa.Column(sa.String)
    hashed_password = sa.Column(sa.String)
    created_date = sa.Column(sa.DateTime, default=datetime.now, index=True)
    last_login = sa.Column(sa.DateTime, default=datetime.now, index=True)
    is_active = sa.Column(sa.Boolean, default=True)

    ratings = relationship("UserRating", back_populates="rated_by")


class UserRating(SqlAlchemyBase):
    __tablename__ = "user_ratings"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    article_id = sa.Column(
        sa.String, sa.ForeignKey("articles.id"), nullable=False, index=True
    )
    value = sa.Column(sa.Float, nullable=False)
    user_id = sa.Column(
        sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True
    )

    rated_by = relationship("User", back_populates="ratings")
