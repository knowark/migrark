from pytest import fixture
from migrark.models import Migration


@fixture
def migration():
    context = {}
    return Migration(context)


def test_migration_instantiation(migration):
    assert migration is not None
