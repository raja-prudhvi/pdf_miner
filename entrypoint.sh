#!/bin/bash

function postgres_ready() {
  pg_isready -h "${DB_HOST}" > /dev/null 2>&1
}

until postgres_ready; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "PostgreSQL is up - executing command"

python manage.py migrate
exec "$@"
