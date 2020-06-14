from pathlib import Path
from migrark.api import sql_migrate


def test_api_sql_migrate(connection):
    target_version = '001'
    migrations_path = str(
        (Path(__file__).parent / 'data' / 'sql' / 'migrations').absolute())
    schema = 'knowark'

    sql_migrate(connection, migrations_path, schema,
                target_version=target_version)

    assert connection._opened == [True]
    assert connection._closed == [True]

    assert connection._execute_statement == (
        'INSERT INTO knowark.__version__ (version) VALUES ($1);'
    )
    assert connection._execute_parameters == ['001']


def test_api_sql_migrate_last(connection):
    migrations_path = str(
        (Path(__file__).parent / 'data' / 'sql' / 'migrations').absolute())
    schema = 'knowark'

    sql_migrate(connection, migrations_path, schema)

    assert connection._opened == [True]
    assert connection._closed == [True]

    assert connection._execute_statement == (
        'INSERT INTO knowark.__version__ (version) VALUES ($1);'
    )
    assert connection._execute_parameters == ['002']
