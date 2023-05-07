class MemoryBlock:
    """
    Represents a contiguous block of memory.
    """
    def __init__(self, start_address, size):
        self.start_address = start_address
        self.size = size