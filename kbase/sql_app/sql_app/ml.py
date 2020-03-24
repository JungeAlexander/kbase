from typing import List

import numpy as np
import torch
from transformers import DistilBertModel, DistilBertTokenizer

from . import models, schemas, tools


model_class, tokenizer_class, pretrained_weights = (
    DistilBertModel,
    DistilBertTokenizer,
    "distilbert-base-cased",
)

# Load pretrained model/tokenizer
tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
model = model_class.from_pretrained(pretrained_weights)


def embed(sentences: List[str]) -> np.ndarray:
    # Not nice but works:
    # encode twice to figure out max. encoded length of the input sentences
    encoded = [tokenizer.encode(s, add_special_tokens=True) for s in sentences]
    max_encoded_len = max((len(e) for e in encoded))
    encoded = [
        tokenizer.encode(
            s,
            add_special_tokens=True,
            max_length=max_encoded_len,
            pad_to_max_length=True,
        )
        for s in sentences
    ]

    input_ids = torch.tensor(
        encoded
    )  # Add special tokens takes care of adding [CLS], [SEP], <s>... tokens in the right way for each model.
    with torch.no_grad():
        last_hidden_states = model(input_ids)[0]  # Models outputs are now tuples
    n = torch.mean(last_hidden_states, 1).numpy()
    return n


def recommend_articles(
    pos_embeddings: np.ndarray, unrated_embeddings: np.ndarray
) -> np.ndarray:
    inner_prods = np.matmul(pos_embeddings, unrated_embeddings.transpose())
    max_prods = np.median(inner_prods, axis=0)
    return max_prods


def recommend(
    user: models.User, articles_recommended: int = 10
) -> List[schemas.Recommendation]:
    pos_articles = tools.get_articles_by_rating(user, score_fun=lambda x: x > 0)
    pos_texts = tools.get_article_texts(pos_articles)
    pos_texts_embedded = embed(pos_texts)

    unreated_articles = tools.get_articles_not_rated(user)
    unrated_texts = tools.get_article_texts(unreated_articles)
    unrated_texts_embedded = embed(unrated_texts)

    recommend_scores = recommend_articles(pos_texts_embedded, unrated_texts_embedded)
    recommend_order = np.argsort(recommend_scores)[::-1]
    recommendations = []
    for i in recommend_order[:articles_recommended]:
        recommendations.append(
            schemas.Recommendation(
                article_id=unreated_articles[i], score=recommend_scores[i]
            )
        )
    return recommendations
