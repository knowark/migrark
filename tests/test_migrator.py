from pytest import fixture
from migrark.versioner import Versioner
from migrark import Migrator


# @fixture
# def collector():
#     return MemoryCollector()


# @fixture
# def versioner():
#     return MemoryVersioner()


# @fixture
# def migrator(versioner, collector):
#     return Migrator(versioner=versioner, collector=collector)


# def test_migrator_instantiation(migrator) -> None:
#     assert migrator is not None


# def test_migrator_migrate(migrator):
#     migrator.migrate()
