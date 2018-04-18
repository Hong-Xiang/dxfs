import unittest
from dxl.fs.path import Path
from dxl.fs.file import File, NotAFileError
from fs.memoryfs import MemoryFS
from fs.tempfs import TempFS

class TestFile(unittest.TestCase):
    def test_exist(self):
        mfs = MemoryFS()
        mfs.touch('test.txt')
        f = File('test.txt', mfs)
        self.assertTrue(f.exists())

    def test_not_exist(self):
        mfs = MemoryFS()
        f = File('test.txt', mfs)
        self.assertFalse(f.exists())

    def test_non_file_error(self):
        mfs = MemoryFS()
        mfs.makedir('test')
        f = File('test', mfs)
        with self.assertRaises(NotAFileError) as target:
            f.exists()

    def test_remove(self):
        with TempFS() as tfs:
            tfs.touch('test')
            f = File('test', tfs)
            self.assertTrue(tfs.exists('test'))
            f.remove()
            self.assertFalse(tfs.exists('test'))