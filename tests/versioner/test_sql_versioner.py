from pytest import fixture
from types import MethodType
from typing import Sequence, List, Dict, Any
from migrark.versioner import SqlVersioner


@fixture
def versioner(connection):
    context = {
        'connection': connection
    }
    return SqlVersioner(context)


def test_sql_versioner_instantiation(versioner):
    assert versioner is not None
    assert versioner.schema == "__template__"
    assert versioner.table == "__version__"
    assert versioner.placeholder == '%s'
    assert versioner.offset == 1


def test_sql_versioner_instantiation_schema_creation(versioner):
    assert versioner.connection._opened == []
    assert versioner.connection._closed == []
    assert versioner.connection._execute_statement == (
        '''CREATE SCHEMA IF NOT EXISTS __template__; '''
        '''CREATE TABLE IF NOT EXISTS __template__.__version__('''
        '''id serial PRIMARY KEY, created_at TIMESTAMP DEFAULT '''
        '''CURRENT_TIMESTAMP, version VARCHAR(255) NOT NULL);'''
    )


def test_sql_versioner_get_version(versioner):
    assert versioner.version == ''
    assert versioner.connection._opened == []
    assert versioner.connection._closed == []
    assert versioner.connection._select_statement == (
        '''SELECT version FROM __template__.__version__ '''
        '''ORDER BY id DESC LIMIT 1'''
    )

    def loaded_select(self, statement: str,
                      parameters: Sequence[Any] = []) -> List[Dict[str, Any]]:
        return [{'version': '003'}]

    versioner.connection.select = MethodType(
        loaded_select, versioner.connection)
    assert versioner.version == '003'


def test_sql_versioner_set_version(versioner):
    versioner.version = '001'

    assert versioner.connection._opened == []
    assert versioner.connection._closed == []
    assert versioner.connection._execute_statement == (
        '''INSERT INTO __template__.__version__ (version) VALUES (%s);'''
    )
    assert versioner.connection._execute_parameters == ['001']


def test_sql_versioner_set_version_index_placeholder(versioner):
    versioner.placeholder = '${index}'
    versioner.version = '001'

    assert versioner.connection._opened == []
    assert versioner.connection._closed == []
    assert versioner.connection._execute_statement == (
        '''INSERT INTO __template__.__version__ (version) VALUES ($1);'''
    )
    assert versioner.connection._execute_parameters == ['001']
