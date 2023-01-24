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
| `ALLOWED_HOSTS` | A list of host/domain names that your Django site is allowed to serve from. If NOT set, the application will reject requests from any domains. | `localhost,otherdomain` |
| `GS_BUCKET_NAME` | Google Storage's bucket name to store uploaded files. If NOT set, the application will store the file locally. | `web_app_bucket` |
| `GS_CREDENTIALS_FILE` | The path to a service account file. if NOT set, it will use GOOGLE_APPLICATION_CREDENTIALS which is typically available in google cloud services. | `/path/bucket_service_account.json` |
