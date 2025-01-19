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
migration:
	poetry run python -m slot_booking_backend.manage makemigrations

.PHONY: superuser
superuser:
	poetry run python -m slot_booking_backend.manage createsuperuser

.PHONY: run-server
run-server:
	poetry run python -m  slot_booking_backend.manage runserver

.PHONY: update
update: install migrate install-pre-commit ;
