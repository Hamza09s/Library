.PHONY: build
build: 
	docker compose build


.PHONY: up
up: 
	docker compose up


.PHONY: down
down: 
	docker compose down


.PHONY: silenceup
silenceup: 
	docker compose up -d

.PHONY: tests
tests: 
	docker compose run --rm web python manage.py test

.PHONY: send_emal
send_email: 
	docker compose run --rm web python manage.py send_email

.PHONY: makemigrations
makemigrations: 
	docker compose run --rm web python manage.py makemigrations


.PHONY: migrate
migrate: 
	docker compose run --rm web python manage.py migrate

.PHONY: createsuperuser
createsuperuser: 
	docker compose run --rm web python manage.py createsuperuser

PHONY: collectstatic
collectstatic: 
	docker compose run --rm web python manage.py collectstatic