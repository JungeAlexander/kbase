from enum import Enum

from datetime import date
from typing import List

from pydantic import BaseModel


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
    link: str
    doid: str = ""
    summary: str = ""
    authors: List[str] = []
    affiliations: List[str] = []
    language: str = ""
    keywords: List[str] = []
    references: List[str] = []

    class Config:
        orm_mode = True


class ArticleCreate(Article):
    pass


class ArticleUpdate(Article):
    pass
