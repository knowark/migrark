from pytest import fixture
from migrark.models import Migration, MemoryMigration


@fixture
def migration():
    context = {}
    return MemoryMigration(context)


def test_migration_instantiation(migration):
    assert migration is not None


def test_memory_migration_version(migration):
    migration = MemoryMigration({}, version='001')

    assert migration.version == '001'


def test_custom_migration_version(migration):
    class CustomMigration(Migration):
        @property
        def version(self):
            return '099'

    migration = CustomMigration({})

    assert migration.version == '099'
