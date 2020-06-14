from typing import Sequence, List, Dict, Any
from pytest import fixture


@fixture
def connection():
    class CustomConnection:
        def __init__(self) -> None:
            self.uri = f"postgresql://postgres:postgres@localhost/migrark"
            self._opened = []
            self._closed = []
            self._execute_statement = ''
            self._execute_parameters = []

        def open(self) -> None:
            self._opened.append(True)

        def close(self) -> None:
            self._closed.append(True)

        def execute(self, statement: str,
                    parameters: Sequence[Any] = []) -> str:
            self._execute_statement = statement
            self._execute_parameters = parameters
            return ''

        def select(self, statement: str,
                   parameters: Sequence[Any] = []) -> List[Dict[str, Any]]:
            self._select_statement = statement
            self._select_parameters = parameters
            return []

    return CustomConnection()
