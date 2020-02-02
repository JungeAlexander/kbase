#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER shareduser WITH
        LOGIN
        NOSUPERUSER
        NOCREATEDB
        NOCREATEROLE
        NOINHERIT
        NOREPLICATION
        PASSWORD '$SHARED_PASSWORD';
    CREATE DATABASE shared OWNER shareduser;
    CREATE USER guest;
    \connect shared;
    GRANT SELECT ON ALL TABLES IN SCHEMA public TO guest;
    GRANT ALL ON ALL TABLES IN SCHEMA public TO shareduser;
EOSQL