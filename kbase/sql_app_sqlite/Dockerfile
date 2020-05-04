FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

#COPY download_model.py /
#RUN ["python", "/download_model.py"]

COPY ./sql_app /app/app
