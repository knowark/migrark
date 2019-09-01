from abc import ABC, abstractmethod


class Collector(ABC):

    @abstractmethod
    def retrieve(self):
        """Retrieve method to be implemented"""
