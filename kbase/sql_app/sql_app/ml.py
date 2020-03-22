from typing import List

from . import models, schemas


def recommend(user: models.User) -> List[schemas.Recommendation]:
    pass
