from abc import ABC, abstractmethod


class MemoryManagerInterface(ABC):
    @abstractmethod
    def allocate(self, size):
        pass

    @abstractmethod
    def deallocate(self, block):
        pass