import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SqlAlchemyBase = declarative_base()

SessionLocal = None


def global_init():
    global SessionLocal

    if SessionLocal:
        return

    password = os.environ["SHARED_PASSWORD"]

    SQLALCHEMY_DATABASE_URL = f"postgresql://shareduser:{password}@postgres:5432/shared"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    from . import models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global SessionLocal

    session: Session = SessionLocal()

    session.expire_on_commit = False

    return session
