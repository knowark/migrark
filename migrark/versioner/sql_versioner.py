from abc import ABC, abstractmethod
from psycopg2 import connect
from .versioner import Versioner


class SqlVersioner(Versioner):
    def __init__(self, uri: str, schema='__template__') -> None:
        self.uri = uri
        self.schema = schema
        self.table = '__version__'
        self._setup()

    @property
    def current_version(self) -> str:
        return ''

    def _setup(self) -> None:
        with connect(self.uri) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f'CREATE SCHEMA IF NOT EXISTS {self.schema}')
                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS {self.schema}.{self.table}("
                    "id serial PRIMARY KEY, "
                    "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "
                    "version VARCHAR(255) NOT NULL);")
