# covid19-multilingue-peru-backend

## Requirements:

- Docker
- Docker Compose

## Build

1. Copy .env-sample to .env
2. Configure the .env file
3. build docker images

   `docker-compose build`

4. Access to the service container

   `docker-compose run --rm --service-ports backend`

5. Setup python virtual environment

   `virtualenv ve && source ve/bin/activate`

6. Install python dependencies

   `pip install -r requirements.txt`

## Run in local

1. Access to the service container

   `docker-compose run --rm --service-ports backend`

2. Access to the virtual environment

   `source ve/bin/activate`

3. Run django server

   `python manage.py runserver 0:8000`
