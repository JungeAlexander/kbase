from typing import Callable, List

from . import main, models


def get_article_texts(article_ids: List[str]) -> List[str]:
    texts = []
    for aid in article_ids:
        article = main.read_article(aid)
        title = article.title.strip()
        if title[-1] not in "!?.":
            title += "."
        summary = article.summary.strip()
        text = title + " " + summary
        texts.append(text)
    return texts


def get_articles_by_rating(
    user: models.User, score_fun: Callable[[float], bool]
) -> List[str]:
    article_ids = []
    for r in user.ratings:
        if score_fun(r.value):
            article_ids.append(r.article_id)
    return article_ids


def get_articles_not_rated(
    user: models.User, articles_returned: int = 100, skip: int = 0, limit: int = 1000
) -> List[str]:
    article_ids = []
    user_id = user.id
    for a in main.read_articles(skip=skip, limit=limit):
        if len(article_ids) >= articles_returned:
            return article_ids
        rated_by_user = False
        for r in a.ratings:
            if user_id == r.user_id:
                rated_by_user = True
                break
        if not rated_by_user:
            article_ids.append(a.id)
    return article_ids
