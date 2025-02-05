install:
	uv sync

brain-games:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install --force-reinstall dist/*.whl

make lint:
	uv run ruff check gendiff