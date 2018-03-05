import unittest
from dxl.fs.base import FileSystem, ObjectOnFileSystem
from fs.errors import FilesystemClosed
from fs.memoryfs import MemoryFS
import fs.base


class TestFileSystem(unittest.TestCase):
    def test_pass_object(self):
        fsc = FileSystem(MemoryFS())
        with fsc.open() as fsi:
            self.assertIsInstance(fsi, fs.base.FS)

    def test_pass_closed_object(self):
        with MemoryFS() as mfs:
            pass
        fsc = FileSystem(mfs)
        with self.assertRaises(FilesystemClosed):
            with fsc.open() as fsi:
                self.assertIsInstance(fsi, fs.base.FS)

    def test_by_class(self):
        fsc = FileSystem(MemoryFS)
        with fsc.open() as fsi:
            self.assertIsInstance(fsi, fs.base.FS)

    def test_copy_init(self):
        fsc = FileSystem(MemoryFS)
        fs2 = FileSystem(fsc)
        with fs2.open() as fsi:
            self.assertIsInstance(fsi, fs.base.FS)


class TestObjectOnFileSystem(unittest.TestCase):
    def test_exist(self):
        mfs = MemoryFS()
        mfs.touch('test.txt')
        afs = FileSystem(mfs)
        o = ObjectOnFileSystem(afs, 'test.txt')
        self.assertTrue(o.exists())

    def test_non_exist(self):
        mfs = MemoryFS()
        afs = FileSystem(mfs)
        o = ObjectOnFileSystem(afs, 'test.txt')
        self.assertFalse(o.exists())
