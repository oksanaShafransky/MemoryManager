from abc import ABC, abstractmethod
from typing import Optional
from memory_block import MemoryBlock


class MemoryManagerInterface(ABC):
    @abstractmethod
    def allocate(self, size: int) -> int:
        pass

    @abstractmethod
    def deallocate(self, address: int) -> None:
        pass

    @abstractmethod
    def write(self, address: int, data: bytes):
        pass

    @abstractmethod
    def read(self, address: int, size: int) -> Optional[bytes]:
        pass