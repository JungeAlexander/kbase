FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./sql_app /app/app
