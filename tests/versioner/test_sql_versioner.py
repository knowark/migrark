from pytest import fixture, mark
from psycopg2 import connect
from migrark.versioner import Versioner, SqlVersioner


pytestmark = mark.sql


@fixture
def versioner(database):
    database_uri = f"postgresql://postgres:postgres@localhost/{database}"
    context = {
        'database_uri': database_uri
    }
    return SqlVersioner(context)


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


def test_sql_versioner_get_version(versioner):
    assert versioner.version == ''


def test_sql_versioner_set_version(versioner):
    versioner.version = '001'

    assert versioner.version == '001'
