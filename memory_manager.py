from typing import Optional

from memeory_manager_interface import MemoryManagerInterface
from memory_block import MemoryBlock

class MemoryManager(MemoryManagerInterface):
    """
    MemoryManager manages allocations and deallocations on a large contiguous block of memory.
    """
    def __init__(self, size):
        """
        Initialize the memory manager with a large contiguous block of memory.
        :param size: size of the contiguous block of memory
        """
        self.memory = bytearray(size)
        self.free_blocks = [MemoryBlock(0, size)]
        self.allocated_blocks = []

    def allocate(self, size) -> int:
        """
        Allocate a block of memory of the given size.
        :param size: size of the block to be allocated
        :return: the starting address of the allocated block
        """
        if size <= 0:
            return None

        # Find the first free block that can accommodate the requested size
        for block in self.free_blocks:
            if block.size >= size:
                # Split the free block into two blocks (allocated and remaining free block)
                new_block = MemoryBlock(block.start_address, size)
                self.allocated_blocks.append(new_block)
                if block.size == size:
                    # The entire free block was allocated, so remove it from the free blocks list
                    self.free_blocks.remove(block)
                else:
                    # Only part of the free block was allocated, so update the free block's start address and size
                    block.start_address += size
                    block.size -= size
                return new_block.start_address

        # Unable to find a free block that can accommodate the requested size
        return None

    def deallocate(self, start_address)->None:
        """
        Deallocate the block of memory starting at the given address.
        :param start_address: starting address of the block to be deallocated
        """
        # Find the allocated block with the given starting address
        for block in self.allocated_blocks:
            if block.start_address == start_address:
                # Remove the allocated block from the allocated blocks list
                self.allocated_blocks.remove(block)
                # Add the freed block to the free blocks list
                self.free_blocks.append(block)
                # Merge adjacent free blocks
                self._merge_free_blocks()
                return

    def _merge_free_blocks(self):
        """
        Merge adjacent free blocks in the free blocks list.
        """
        # Sort the free blocks list by start address
        self.free_blocks.sort(key=lambda block: block.start_address)
        # Merge adjacent free blocks
        i = 0
        while i < len(self.free_blocks) - 1:
            curr_block = self.free_blocks[i]
            next_block = self.free_blocks[i + 1]
            if curr_block.start_address + curr_block.size == next_block.start_address:
                # The current block and next block are adjacent, so merge them into one block
                merged_block = MemoryBlock(curr_block.start_address, curr_block.size + next_block.size)
                self.free_blocks[i] = merged_block
                del self.free_blocks[i + 1]
            else:
                # The current block and next block are not adjacent, so move on to the next block
                i += 1

    def read(self, address: int, size: int)-> Optional[bytes]:
        # Read the specified number of bytes starting from the given start address
        return bytes(self.memory[address:address + size])

    def write(self, address: int, data: int):
        # Write the given data to the memory starting at the given start address
        self.memory[address:address + len(data)] = data
