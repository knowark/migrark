from pytest import fixture, mark
from psycopg2 import connect
from migrark.versioner import Versioner, SqlVersioner


pytestmark = mark.sql


@fixture(scope="session")
def database():
    database = "migrark"
    postgres_dsn = f"dbname=postgres user=postgres password=postgres"
    with connect(postgres_dsn) as connection:
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("DROP DATABASE IF EXISTS migrark")
            cursor.execute("CREATE DATABASE migrark")

    return database


@fixture
def versioner(database):
    uri = f"postgresql://postgres:postgres@localhost/{database}"
    return SqlVersioner(uri=uri)


def test_sql_versioner_instantiation(versioner, database):
    assert versioner is not None
    assert versioner.uri == (
        f"postgresql://postgres:postgres@localhost/{database}")
    assert versioner.schema == "__template__"


def test_sql_versioner_instantiation_schema_creation(versioner):
    with connect(versioner.uri) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT schema_name FROM information_schema.schemata')
            schemas = [row[0] for row in cursor.fetchall()]

    assert '__template__' in schemas


def test_sql_versioner_instantiation_version_table_creation(versioner):
    with connect(versioner.uri) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT tablename FROM pg_catalog.pg_tables "
                "WHERE schemaname = '__template__'")
            tables = [row[0] for row in cursor.fetchall()]

        with connection.cursor() as cursor:
            cursor.execute("SELECT column_name "
                           "FROM information_schema.columns "
                           "WHERE table_schema = '__template__' "
                           "AND table_name = '__version__'")
            columns = [row[0] for row in cursor.fetchall()]

    assert '__version__' in tables
    assert 'id' in columns
    assert 'created_at' in columns
    assert 'version' in columns
