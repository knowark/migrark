from abc import ABC, abstractmethod


class Versioner(ABC):

    @property
    @abstractmethod
    def current_version(self) -> str:
        """Retrieve method to be implemented"""


class MemoryVersioner(Versioner):
    def __init__(self, version: str = '') -> None:
        self._version = version

    @property
    def current_version(self) -> str:
        return self._version
