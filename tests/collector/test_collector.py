from pytest import fixture
from migrark.collector import Collector
from migrark.models import Migration
from migrark.collector import MemoryCollector


def test_collector_methods() -> None:
    methods = Collector.__abstractmethods__  # type: ignore
    assert 'retrieve' in methods


# @fixture
# def memory_collector():
#     migrations = [
#         Migration(),
#         Migration(),
#         Migration()
#     ]
#     return MemoryCollector(migrations)


# def test_memory_collector_retrieve():
