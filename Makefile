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

coverage: 
	export COVERAGE_FILE=$(COVFILE); pytest -x --cov=migrark tests/ \
	--cov-report term-missing -s -o cache_dir=/tmp/.pytest_cache

coverage-offline: 
	mypy tenark
	export COVERAGE_FILE=$(COVFILE); pytest -x -m "not sql" --cov=tenark \
	tests/ --cov-report term-missing -s -o cache_dir=/tmp/.pytest_cache

mypy-coverage: mypy coverage

PART ?= patch

version:
	bump2version $(PART) pyproject.toml migrark/__init__.py --tag --commit

devdeploy:
	# Run as root in the development server
	sudo apt update
	sudo apt install -y python3-pip postgresql postgresql-server-dev-all
	sudo python3 -m pip install mypy pytest pytest-cov psycopg2
	sudo -Hiu postgres psql -c "ALTER USER postgres WITH PASSWORD 'postgres';"
	# Modify pg_hba.conf file
	sed -i "s/local   all             \
	postgres                                peer\
	/local   all             \
	postgres                                md5/g" \
	/etc/postgresql/10/main/pg_hba.conf
	# Restart Postgresql Server
	sudo service postgresql restart