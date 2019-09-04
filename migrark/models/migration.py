from abc import ABC, abstractmethod
from typing import Dict, Any


class Migration:
    version = None

    def __init__(self, context: Dict[str, Any]) -> None:
        self._version = context.get('version', '')

    @property
    def version(self) -> str:
        return self._version
