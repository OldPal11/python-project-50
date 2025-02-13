install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install --force-reinstall dist/*.whl

test:
	uv run pytest --maxfail=5 --disable-warnings

lint:
	uv run ruff check gendiff

check:
	make lint 
	make test