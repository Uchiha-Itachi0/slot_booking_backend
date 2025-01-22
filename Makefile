.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m slot_booking_backend.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m slot_booking_backend.manage makemigrations

.PHONY: superuser
superuser:
	poetry run python -m slot_booking_backend.manage createsuperuser

.PHONY: run-server
run-server:
	poetry run python -m  slot_booking_backend.manage runserver

.PHONY: run-server-with-migrations
run-server-with-migrations:
	poetry run python -m slot_booking_backend.manage migrate
	poetry run python -m slot_booking_backend.manage makemigrations
	poetry run python -m  slot_booking_backend.manage runserver



.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker-compose down
	docker-compose -f docker-compose.dev.yml up --build --force-recreate db app

.PHONY: up-dependencies-db-only
up-dependencies-db-only:
	test -f .env || touch .env
	docker-compose down
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: update
update: install migrate install-pre-commit ;
