from pytest import fixture
from migrark.models import Migration
from migrark.versioner import MemoryVersioner
from migrark.collector import MemoryCollector
from migrark import Migrator


@fixture
def collector():
    migrations = [
        Migration({'version': '001'}),
        Migration({'version': '002'}),
        Migration({'version': '003'})
    ]
    return MemoryCollector(migrations)


@fixture
def versioner():
    return MemoryVersioner()


@fixture
def migrator(versioner, collector):
    return Migrator(versioner=versioner, collector=collector)


def test_migrator_instantiation(migrator) -> None:
    assert migrator is not None


def test_migrator_migrate(migrator):
    migrator.migrate()

    collector = migrator.collector

    for migration in collector.retrieve():
        assert migration._schema_up is True


def test_migrator_migrate_to_upper_version(migrator):
    migrator.versioner._version = '002'

    migrator.migrate()

    migrations = migrator.collector.retrieve()
    assert migrations[0]._schema_up is False
    assert migrations[1]._schema_up is False
    assert migrations[2]._schema_up is True


def test_migrator_migrate_to_target_version(migrator):
    migrator.migrate('002')

    migrations = migrator.collector.retrieve()
    assert migrations[0]._schema_up is True
    assert migrations[1]._schema_up is True
    assert migrations[2]._schema_up is False


def test_migrator_migrate_to_lower_version(migrator):
    migrator.versioner._version = '002'

    migrator.migrate('001')

    migrations = migrator.collector.retrieve()
    assert migrations[0]._schema_down is True
    assert migrations[1]._schema_down is False
    assert migrations[2]._schema_down is False


def test_migrator_migrate_to_equal_version(migrator):
    migrator.versioner._version = '002'

    migrator.migrate('002')

    migrations = migrator.collector.retrieve()
    assert migrations[0]._schema_up is False
    assert migrations[1]._schema_up is False
    assert migrations[2]._schema_up is False
    assert migrations[0]._schema_down is False
    assert migrations[1]._schema_down is False
    assert migrations[2]._schema_down is False
