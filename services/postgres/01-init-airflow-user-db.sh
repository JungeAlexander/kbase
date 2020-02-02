#!/bin/bash
set -e # exit if a command exits with a not-zero exit code

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER airflow WITH
      LOGIN
      NOSUPERUSER
      NOCREATEDB
      NOCREATEROLE
      NOINHERIT
      NOREPLICATION
      PASSWORD '$AIRFLOW_PASSWORD';
  CREATE DATABASE airflow OWNER airflow;
EOSQL

