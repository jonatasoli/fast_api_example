.PHONY: install update shell format lint test sec export configs upgrade run migrate


install:
	@poetry install

update:
	@poetry update

shell:
	@poetry shell

format:
	@blue .
	@isort .

lint:
	@black . --check
	@isort . --check
	rm -rf .mypy_cache/
	@mypy .
	@pylint .

test:
	@pytest -s .

configs:
	dynaconf -i src.config.settings list

upgrade:
	@poetry run alembic upgrade head

run:
	@poetry run uvicorn main:create_app --factory --reload --host 0.0.0.0 --port 8000

migrate:
	@poetry run alembic revision --autogenerate
