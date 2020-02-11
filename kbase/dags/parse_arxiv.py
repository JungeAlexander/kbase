import logging
import os
from datetime import date
from datetime import datetime, timedelta
from time import mktime, sleep

import arxiv
import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from schemas import ArticleCreate, ArticleType, Article, ArticleUpdate

logging.basicConfig(level=logging.INFO)


# TODO get those updated over last hour?
def parse_arxix(input_query: str) -> None:
    sleep(10)
    query = arxiv.query(
        query=input_query,
        max_results=10,
        iterative=True,
        # max_chunk_results=10,
        sort_by="lastUpdatedDate",
    )

    for res in query():
        d = {}
        _id, version = res["id"].split("/")[-1].split("v")
        d["id"] = "arXiv:" + _id
        d["version"] = "v" + version
        d["source"] = "arXiv"
        d["journal"] = "arXiv"
        d["article_type"] = ArticleType.preprint
        d["title"] = " ".join(res["title"].split())
        d["publication_date"] = date.fromtimestamp(mktime(res["published_parsed"]))
        d["update_date"] = date.fromtimestamp(mktime(res["updated_parsed"]))
        d["summary"] = " ".join(res["summary"].split())
        d["link"] = res["arxiv_url"]
        d["authors"] = res["authors"]
        if res["affiliation"] != "None":
            d["affiliations"] = [res["affiliation"]]
        d["language"] = "en"
        tags = []
        for tag in res["tags"]:
            tags.append(tag["term"])
        d["keywords"] = tags

        get_r = requests.get(f"http://sql_app:8087/articles/{d['id']}")
        if get_r.status_code == 200:
            # existing_article = Article.parse_raw(get_r.text)
            payload = ArticleUpdate(**d).json()
            put_r = requests.put(
                f"http://sql_app:8087/articles/{d['id']}", data=payload
            )
            if put_r.status_code != 200:
                logging.warning(
                    f"PUT failed with code {put_r.status_code} {put_r.json()} for:{os.linesep}{payload}"
                )
        elif get_r.status_code == 404:
            payload = ArticleCreate(**d).json()
            post_r = requests.post("http://sql_app:8087/articles/", data=payload)
            if post_r.status_code != 200:
                logging.warning(
                    f"POST failed with code {post_r.status_code} {post_r.json()} for:{os.linesep}{payload}"
                )
        else:
            logging.warning(
                f"GET failed with code {get_r.status_code} {get_r.json()} for:{os.linesep}{d}"
            )


default_args = {
    "owner": "Airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 1, 23),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    "ingest_arxiv",
    default_args=default_args,
    schedule_interval="@hourly",
    catchup=False,
)

# see https://arxiv.org/help/api/user-manual#subject_classifications
categories = (
    "cs.AI",
    "cs.IR",
    "stat.ML",
    "q-bio.BM",
    "q-bio.CB",
    "q-bio.GN",
    "q-bio.MN",
    "q-bio.NC",
    "q-bio.OT",
    "q-bio.PE",
    "q-bio.QM",
    "q-bio.SC",
    "q-bio.TO",
)
for cat in categories:
    _ = PythonOperator(
        task_id=f"parse_arxix_{cat}",
        python_callable=parse_arxix,
        op_kwargs={"input_query": f"cat:{cat}"},
        dag=dag,
    )
