from abc import ABC, abstractmethod


class Table(ABC):

    @abstractmethod
    def set_table(self, table):
        pass

    @abstractmethod
    def solve(self):
        pass