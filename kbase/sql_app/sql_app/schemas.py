from enum import Enum

from datetime import date, datetime
from typing import List

from pydantic import BaseModel, EmailStr


class UserRatingBase(BaseModel):
    value: float


class UserRatingCreate(UserRatingBase):
    article_id: str
    user_id: int


class UserRating(UserRatingCreate):
    id: int
    modified_date: datetime

    class Config:
        orm_mode = True


class UserRatingUpdate(UserRatingBase):
    pass


class ArticleType(str, Enum):
    preprint = "preprint"
    postprint = "postprint"
    proceeding = "proceeding"


class Article(BaseModel):
    id: str
    version: str
    source: str
    journal: str
    article_type: ArticleType
    title: str
    publication_date: date
    update_date: date
    modified_date: datetime
    link: str
    doid: str = ""
    summary: str = ""
    authors: List[str] = []
    affiliations: List[str] = []
    language: str = ""
    keywords: List[str] = []
    references: List[str] = []
    ratings: List[UserRating] = []

    class Config:
        orm_mode = True


class ArticleCreate(Article):
    pass


class ArticleUpdate(Article):
    pass


class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(UserBase):
    password: str


# TODO how to password changes/reset?
class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    created_date: datetime
    last_login: datetime
    is_active: bool
    ratings: List[UserRating] = []

    class Config:
        orm_mode = True
