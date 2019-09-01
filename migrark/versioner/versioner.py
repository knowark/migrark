from abc import ABC, abstractmethod


class Versioner(ABC):

    @property
    @abstractmethod
    def current_version(self):
        """Retrieve method to be implemented"""
