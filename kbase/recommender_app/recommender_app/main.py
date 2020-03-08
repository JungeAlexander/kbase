from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


app = FastAPI(
    title="recommend", description="recommend articles to read", version="v1",
)

origins = ["http://localhost:8080", "http://localhost:8088"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def embed():
    return {"Hello": "World"}


# POST embed
# Input: - json containing list of strings to
#        - embedding type
# Output: list of embeddings

# GET recommend
# Input: user id
# Output: recommended articles
