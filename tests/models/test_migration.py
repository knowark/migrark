from pytest import fixture
from migrark.models import Migration


@fixture
def migration():
    context = {}
    return Migration(context)


def test_migration_instantiation(migration):
    assert migration is not None


def test_memory_migration_version(migration):
    migration = Migration({'version': '001'})

    assert migration.version == '001'


def test_memory_migration_schema_up(migration):
    migration = Migration({'version': '001'})

    migration.schema_up()

    assert migration._schema_up is True


def test_memory_migration_schema_down(migration):
    migration = Migration({'version': '002'})

    migration.schema_down()

    assert migration._schema_down is True


def test_custom_migration_version(migration):
    class CustomMigration(Migration):
        @property
        def version(self):
            return '099'

    migration = CustomMigration({})

    assert migration.version == '099'
