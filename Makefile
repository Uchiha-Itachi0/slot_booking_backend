.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m slot-booking-backend.manage migrate

.PHONY: migrations
migration:
	poetry run python -m slot-booking-backend.manage makemigrations

.PHONY: superuser
superuser:
	poetry run python -m slot-booking-backend.manage createsuperuser

.PHONY: run-server
run-server:
	poetry run python -m  slot-booking-backend.manage runserver

.PHONY: update
update: install migrate ;

