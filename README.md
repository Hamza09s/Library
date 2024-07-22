1-install docker : https://docs.docker.com/engine/install/
2- build requirements and open container with docker compose up --build
3- run and create migrations with docker compose run --rm web python manage.py makemigrations and then docker compose run --rm web python manage.py migrate
4- now you can go to site at http://127.0.0.1:8000/

Future work:
Lack of time lead t not being able to set up email although celery beat is set uo for scheduled tasks
improve ui design
