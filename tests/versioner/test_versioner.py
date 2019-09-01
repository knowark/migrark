from pytest import fixture
from migrark.versioner import Versioner


def test_versioner_methods() -> None:
    methods = Versioner.__abstractmethods__  # type: ignore
    assert 'current_version' in methods
