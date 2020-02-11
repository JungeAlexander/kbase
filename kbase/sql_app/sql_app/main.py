from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware


from . import crud, schemas
from .database import create_session, global_init

global_init()

app = FastAPI(
    title="kbase article store",
    description="Retrieve and update articles in kbase.",
    version="v1",
)

origins = ["http://localhost:8080", "http://localhost:8088"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = None
    try:
        db = create_session()
        yield db
    finally:
        db.close()


@app.post("/articles/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    article_id = article.id
    db_article = crud.get_article(db, article_id=article_id)
    if db_article:
        raise HTTPException(
            status_code=400, detail=f"Article with id {article_id} already registered"
        )
    return crud.create_article(db=db, article=article)


@app.put("/articles/{article_id}", response_model=schemas.Article)
def update_article(
    article_id: str, article: schemas.ArticleUpdate, db: Session = Depends(get_db)
):
    db_article = crud.get_article(db, article_id=article_id)
    if not db_article:
        raise HTTPException(
            status_code=400, detail=f"Article with id {article_id} does not exist"
        )
    return crud.update_article(db=db, article=article)


@app.get("/articles/", response_model=List[schemas.Article])
def read_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = crud.get_articles(db, skip=skip, limit=limit)
    return articles


@app.get("/articles/{article_id}", response_model=schemas.Article)
def read_article(article_id: str, db: Session = Depends(get_db)):
    db_article = crud.get_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail=f"Email {user.email} already registered."
        )
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User ID {user_id} not found")
    return db_user


@app.post(
    "/users/{user_id}/user_ratings/{article_id}", response_model=schemas.UserRating
)
def create_rating_for_user(
    user_id: int,
    article_id: str,
    user_rating: schemas.UserRatingCreate,
    db: Session = Depends(get_db),
):
    return crud.create_user_rating(
        db=db, user_rating=user_rating, user_id=user_id, article_id=article_id
    )


@app.get("/user_ratings/", response_model=List[schemas.UserRating])
def read_user_ratings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_ratings = crud.get_user_ratings(db, skip=skip, limit=limit)
    return user_ratings
