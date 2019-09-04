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


def test_custom_migration_version(migration):
    class CustomMigration(Migration):
        @property
        def version(self):
            return '099'

    migration = CustomMigration({})

    assert migration.version == '099'
