from typing import Callable, List

from . import crud, main, models


def get_article_texts(article_ids: List[str]) -> List[str]:
    texts = []
    for aid in article_ids:
        article: models.Article = main.read_article(aid)
        title = article.title
        if title[-1] not in "!?.":
            title += "."
        summary = article.summary.strip()
        text = title + " " + summary
        texts.append(text)
    return texts


def get_articles_by_rating(
    user: models.User, score_fun: Callable[[float], bool]
) -> List[str]:
    pass


def get_articles_not_rated(user: models.User) -> List[str]:
    pass
