from pytest import fixture
from migrark.versioner import Versioner, MemoryVersioner


def test_versioner_methods() -> None:
    methods = Versioner.__abstractmethods__  # type: ignore
    assert 'current_version' in methods


def test_memory_versioner_current_version():
    versioner = MemoryVersioner('001')
    assert versioner.current_version == '001'
