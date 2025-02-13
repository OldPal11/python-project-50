install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install --force-reinstall dist/*.whl

make lint:
	uv run ruff check gendiff

test:
	uv run pytest --maxfail=5 --disable-warnings

check:
	lint test

lint:
	uv run ruff check gendiff