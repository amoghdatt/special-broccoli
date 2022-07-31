from abc import ABC, abstractmethod


class Rule(ABC):

    @abstractmethod
    def apply(self):
        pass
