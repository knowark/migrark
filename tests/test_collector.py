from pytest import fixture
from migrark.collector import Collector


def test_collector_methods() -> None:
    methods = Collector.__abstractmethods__  # type: ignore
    assert 'retrieve' in methods
