# MemoryManager

## Implementation Description:
The memory manager is implemented as a class, MemoryManager, successor of abstract class MemoryManagerInterface, which has two main methods, allocate, deallocate, read and write.
The MemoryManager class takes a single argument block_size in the constructor, which represents the size of the contiguous block of memory that the manager will manage.
When an instance of the MemoryManager class is created, it creates a bytearray of a specified size and uses that as the memory block to allocate and deallocate from.
This makes the class self-contained and independent of any external memory blocks that may exist.
- The allocate method takes a single argument size and returns a pointer to a block of memory of at least that size, or None if there is not enough free memory to satisfy the request.
- The deallocate method takes a single argument ptr, which is a pointer to a previously allocated block of memory.
- read - reads the specified number of bytes from the block of memory starting from specified start_address.
- write - writes the specified data into the block of memory with the specified block size starting from specified start_address. 
          write method assumes that before its call, the memory is allocated and verified there is enough space (like used in test).

The MemoryManager class keeps track of the free blocks of memory using a list of tuples, where each tuple represents a contiguous block of free memory and contains the starting address and length of the block.

## Algorithm:
When a request to allocate memory comes in, the allocate method iterates over the list of free blocks and returns the first block that is large enough to satisfy the request.
If there are no free blocks that are large enough, allocate returns None.
When a block of memory is deallocated using the deallocate method, the manager checks if the freed block can be merged with any adjacent free blocks.
If so, the blocks are merged into one larger free block. If not, the freed block is added to the list of free blocks.

The memory manager is implemented using a simple first-fit allocation algorithm and a list of tuples to represent the free blocks of memory.
## Pros:
One advantage of this approach is its simplicity. It is easy to understand and implement, which makes it a good choice for smaller programs or programs with less demanding memory requirements.
Another advantage of this approach is its flexibility. The MemoryManager class provides an abstraction layer that makes it easy to swap in a different memory allocation algorithm in the future if needed.
This can be especially useful if the program's memory requirements change over time and a more sophisticated memory allocation algorithm becomes necessary.

## Cons:
One potential disadvantage of this approach is that it may not be as efficient as other memory allocation algorithms in terms of both time and space complexity.
For example, the first-fit algorithm may result in more fragmentation of the memory space, which can reduce the efficiency of memory usage.
Additionally, the list of tuples used to represent free memory blocks can become inefficient as the number of blocks grows large.
Overall, the choice of memory allocation algorithm and data structure will depend on the specific needs of the program, such as the size of the memory space, the frequency of memory allocations and deallocations, and the tradeoff between memory efficiency and time complexity.

## Possible Optimizations:
One possible optimization is to keep the list of free blocks sorted by address. This would make it faster to find adjacent free blocks to merge with when deallocating memory.
Another optimization is to implement a best-fit algorithm for allocating memory, where the manager finds the free block that is closest in size to the requested size.
This can help reduce fragmentation of the memory over time.
Another optimization is to implement a garbage collector that periodically scans the allocated memory to identify and free blocks of memory that are no longer being used.

One potential issue with the current design is that it assumes a contiguous block of memory that is allocated at startup and never changes.
In a real-world scenario, it is possible that the memory manager would need to handle dynamic allocation and deallocation of memory as the program runs.
Another consideration is that the current implementation does not take into account the possibility of multiple threads or processes accessing the memory manager simultaneously.
In a multi-threaded/multi-process environment, it would be necessary to implement some kind of synchronization mechanism to ensure that memory is not allocated or deallocated incorrectly.

