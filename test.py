import unittest
import pytest

from memory_manager import MemoryManager

class TestMemoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = MemoryManager(1024)

    def test_allocate_deallocate(self):
        addr1 = self.manager.allocate(512)
        self.assertIsNotNone(addr1)
        addr2 = self.manager.allocate(512)
        self.assertIsNotNone(addr2)
        result1 = self.manager.deallocate(addr1)
        self.assertIsNone(result1)
        result2 = self.manager.deallocate(addr2)
        self.assertIsNone(result2)

    def test_allocate_entire_block(self):
        ptr = self.manager.allocate(1024)
        self.assertEqual(ptr, 0)

    def test_allocate_beyond_block_size(self):
        ptr = self.manager.allocate(2048)
        self.assertIsNone(ptr)

    def test_deallocate_invalid_pointer(self):
        ptr = self.manager.allocate(256)
        result = self.manager.deallocate(ptr+1)
        self.assertFalse(result)

    def test_deallocate_already_freed_pointer(self):
        ptr = self.manager.allocate(256)
        self.manager.deallocate(ptr)
        result = self.manager.deallocate(ptr)
        self.assertFalse(result)

    def test_read_write(self):
        block = self.manager.allocate(21)
        self.assertIsNotNone(block)
        msg = b'This is MemoryManager'
        self.manager.write(block, msg)
        data = self.manager.read(block, 21)
        assert data == msg


