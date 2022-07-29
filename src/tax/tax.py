from abc import ABC, abstractmethod


class Tax(ABC):

    @abstractmethod
    def compute(self):
        pass
