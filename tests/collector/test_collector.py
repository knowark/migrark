from pytest import fixture
from migrark.collector import Collector
from migrark.models import Migration
from migrark.collector import MemoryCollector


def test_collector_methods() -> None:
    methods = Collector.__abstractmethods__  # type: ignore
    assert 'retrieve' in methods


@fixture
def memory_collector():
    migrations = [
        Migration({'version': '001'}),
        Migration({'version': '002'}),
        Migration({'version': '003'})
    ]
    return MemoryCollector(migrations)


def test_memory_collector_retrieve(memory_collector):
    migrations = memory_collector.retrieve()
    assert migrations[0].version == '001'
    assert migrations[1].version == '002'
    assert migrations[2].version == '003'
