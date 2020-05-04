docker build -t sql_app_sqlite:latest .
docker run -p 80:80 sql_app_sqlite:latest