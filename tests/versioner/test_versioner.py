from pytest import fixture
from migrark.versioner import Versioner, MemoryVersioner


def test_versioner_methods() -> None:
    methods = Versioner.__abstractmethods__  # type: ignore
    assert 'version' in methods


def test_memory_versioner_get_version():
    versioner = MemoryVersioner('001')
    assert versioner.version == '001'


def test_memory_versioner_set_version():
    versioner = MemoryVersioner('001')

    versioner.version = '002'

    assert versioner.version == '002'
