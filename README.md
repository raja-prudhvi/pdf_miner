# PDF miner

A Python server that renders the user interface, accepts files from users, and extracts text from PDFs.

![Screenshot of the application](/demo.png?raw=true "Demo")

## Getting started


Running locally using Python

```

> cd pdf_miner/

> python3 -m venv .venv

> source .venv/bin/activate

> pip install -r requirements.txt

> cp .env.example .env

> python manage.py migrate

> python manage.py runserver

```

Running locally using Docker
```
> cd pdf_miner/

> docker-compose build

> docker-compose up
```

You can access the server on http://localhost:8000

## Environment variables

| Key         | Description | Example |
| -----------  | ----------- |----------- |
| `SECRET_KEY` | A string that is used to provide cryptographic signing, and should be kept secret. If NOT set, the application will not be executed. | `django-insecure-d462upu)4h4fx!8vl1%g+^#rjk)m#y^1tsul89bq^ttgni+9k=` |
| `DB_URL` | The connection string to the database. It must be either sqlite or postgres. If NOT set, the application will not execute. You can use sqlite while you don’t have a postgres database set. | `postgres://user:password@host:port/dbname` |
