from pathlib import Path
from pytest import fixture
from migrark.collector import Collector
from migrark.models import Migration
from migrark.collector import DirectoryCollector


@fixture
def directory_collector():
    context = {'path': str(Path(__file__).parent / 'migrations')}
    return DirectoryCollector(context)


def test_directory_collector_retrieve(directory_collector):
    migrations = directory_collector.retrieve()
    assert migrations[0].version == '001'
    assert migrations[1].version == '002'
    assert migrations[2].version == '003'
