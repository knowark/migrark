from pytest import fixture
from psycopg2 import connect


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
