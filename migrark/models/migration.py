from abc import ABC, abstractmethod
from typing import Dict, Any


class Migration(ABC):
    def __init__(self, context: Dict[str, Any]):
        self.context = context

    @property
    @abstractmethod
    def version(self) -> str:
        """Version property to be implemented"""


class MemoryMigration(Migration):
    def __init__(self, context: Dict[str, Any], version=''):
        super().__init__(context)
        self._version = version

    @property
    def version(self) -> str:
        return self._version
