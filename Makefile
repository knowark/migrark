clean:
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +
	find . -name '.mypy_cache' -exec rm -fr {} +
	find . -name 'pip-wheel-metadata' -exec rm -fr {} +
	find . -name 'migrark.egg-info' -exec rm -fr {} +

test:
	pytest

mypy: 
	mypy migrark

COVFILE ?= .coverage

coverage: mypy
	export COVERAGE_FILE=$(COVFILE); pytest -x --cov-branch --cov=migrark \
	tests/ --cov-report term-missing -s -o cache_dir=/tmp/.pytest_cache


PART ?= patch

version:
	bump2version $(PART) pyproject.toml migrark/__init__.py --tag --commit
