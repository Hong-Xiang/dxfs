import unittest
from dxl.dxfs.base import FileSystem
from fs.errors import FilesystemClosed
from fs.memoryfs import MemoryFS


class TestFileSystem(unittest.TestCase):
    def test_pass_object(self):
        fs = FileSystem(MemoryFS())
        with fs.open():
            pass

    def test_pass_closed_object(self):
        with MemoryFS() as mfs:
            pass
        fs = FileSystem(mfs)
        with self.assertRaises(FilesystemClosed):
            with fs.open():
                pass
