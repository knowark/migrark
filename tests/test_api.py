from pathlib import Path
from psycopg2 import connect
from migrark.api import sql_migrate


def test_api_sql_migrate(database):
    target_version = '001'
    migrations_path = str(
        (Path(__file__).parent / 'data' / 'sql' / 'migrations').absolute())
    database_uri = f"postgresql://postgres:postgres@localhost/{database}"
    schema = 'knowark'

    sql_migrate(database_uri, migrations_path, schema,
                target_version=target_version)

    with connect(database_uri) as c, c.cursor() as cursor:
        query = (f"SELECT version FROM {schema}.__version__ "
                 "ORDER BY created_at DESC LIMIT 1")
        cursor.execute(query)
        result = cursor.fetchone()
        version = result and next(iter(result)) or ''

    assert version == '001'


def test_api_sql_migrate_last(database):
    target_version = '001'
    migrations_path = str(
        (Path(__file__).parent / 'data' / 'sql' / 'migrations').absolute())
    database_uri = f"postgresql://postgres:postgres@localhost/{database}"
    schema = 'knowark'

    sql_migrate(database_uri, migrations_path, schema)

    with connect(database_uri) as c, c.cursor() as cursor:
        query = (f"SELECT tablename FROM pg_catalog.pg_tables "
                 "WHERE schemaname='knowark' ")
        cursor.execute(query)
        result = [row[0] for row in cursor.fetchall()]

    assert 'employees' in result
    assert 'accounts' in result

    with connect(database_uri) as c, c.cursor() as cursor:
        query = (f"SELECT version FROM {schema}.__version__ "
                 "ORDER BY created_at DESC LIMIT 1")
        cursor.execute(query)
        result = cursor.fetchone()
        version = result and next(iter(result)) or ''

    assert version == '002'
