from datetime import date
from typing import List

import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import ARRAY

from .database import SqlAlchemyBase


class Article(SqlAlchemyBase):
    __tablename__ = "articles"

    id: str = sa.Column(sa.String, primary_key=True)
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
