#!/bin/bash

python manage.py collectstatic --noinput

# Check if DB_URL is set, and if it points to PostgreSQL
if [ -n "$DB_URL" ] && [[ "$DB_URL" == postgres* ]]; then
  function postgres_ready() {
    pg_isready -h "${DB_HOST}" > /dev/null 2>&1
  }

  until postgres_ready; do
    >&2 echo "PostgreSQL is unavailable - sleeping"
    sleep 1
  done

  >&2 echo "PostgreSQL is up - executing command"
else
  >&2 echo "Using SQLite - no need to wait for PostgreSQL"
fi

python manage.py migrate
python manage.py loaddata fixture.json
exec "$@"
