# Querying arXiv preprints using Apache Airflow

An Apache Airflow pipeline to
download recent articles from the arXiv preprint server.
Articles are stored in a PostgreSQL database via a
custom REST API based on [FastAPI](https://github.com/tiangolo/fastapi).
This API uses [SQLAlchemy](https://www.sqlalchemy.org) as an Object Relational Mapper
as well as [Pydantic](https://github.com/samuelcolvin/pydantic/) models to define the API endpoints.

The setup looks like this:

![Overview](https://github.com/JungeAlexander/kbase/blob/arxiv_airflow_fastapi_psql/doc/img/overview.png)

## Usage

Requires [Docker Compose](https://docs.docker.com/compose/install/).

```sh
docker-compose up -d postgres  # start database first
docker-compose up --build  # then start airflow and the database API
```

## Components

DAGs specifying Airflow pipelines are stored in `kbase/dags/`.
The DAG specified in `kbase/dags/parse_arxiv.py` contains code querying arxiv.org.
Once an hour, the pipeline requests the latest arXiv preprints from a range of categories
related to machine learning and quantitative biology.
To be nice to the public arXiv REST API, only the 10 most recent articles per arXiv category
are requested, a sleep delay between requests is added, and requests are submitted sequentially
via Airflow's
[SequentialExecutor](https://airflow.apache.org/docs/stable/_api/airflow/executors/index.html#airflow.executors.SequentialExecutor).

The Airflow webserver UI is available at: http://localhost:8080

In the UI you can toggle the arXiv pipeline `ingest_arxiv` to "on".

Swagger docs for the database API are available at: http://localhost:80/docs

Code for the API is under `kbase/sql_app`.

JupyterLab is available at: http://localhost:10000/lab

Jupyter Notebook is available at: http://localhost:10000/

## Development

Note: setting this up is only required for active development, not for running the code (see Usage for this part).

Using Python version as in `.python-version`.
Setting up a virtual environment:

```sh
python -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
```

Starting a specific service via docker-compose:

```sh
docker-compose up -d --no-deps --build vue_app
```

Backup data in postgres database:

```sh
docker run --rm -v kbase_pgdata:/volume -v /Users/alexanderjunge/Code/kbase/mybackup:/backup alpine tar -cjf /backup/pgdata_archive.tar.bz2 -C /volume ./
```

Restore data:

```sh
docker run --rm -v kbase_pgdata:/volume -v /Users/alexanderjunge/Code/kbase/mybackup:/backup alpine sh -c "rm -rf /volume/* /volume/.* ; tar -C /volume/ -xjf /backup/pgdata_archive.tar.bz2"
```