import unittest
from fs.memoryfs import MemoryFS
from dxl.fs.directory import Directory


class TestDirectory(unittest.TestCase):
    def test_exist(self):
        mfs = MemoryFS()
        mfs.makedir('test')
        d = Directory('test', mfs)
        self.assertTrue(d.exists())

    def test_not_exist(self):
        mfs = MemoryFS()
        d = Directory('test', mfs)
        self.assertFalse(d.exists())

    def test_not_a_directory(self):
        mfs = MemoryFS()
        mfs.touch('test')
        d = Directory('test', mfs)
        with self.assertRaises(NotADirectoryError):
            d.exists()

    def test_listdir(self):
        mfs = MemoryFS()
        mfs.touch('test_file.txt')
        mfs.makedir('test_dir')
        d = Directory('.', mfs)
        result = []
        d.listdir().subscribe(result.append)
        self.assertEqual(len(result), 2)
        cdir = None
        cfile = None
        for o in result:
            if isinstance(o, Directory):
                cdir = o
            else:
                cfile = o
        self.assertIsNotNone(cdir)
        self.assertIsNotNone(cfile)
        self.assertEqual(cdir.path.n, 'test_dir')
        self.assertEqual(cfile.path.n, 'test_file.txt')

    # def test_check_pos_deffac(self):
    #     assert fi.Directory.check(self.root + '/sub1', FileSystem)

    # def test_check_neg(self):
    #     assert not fi.Directory.check(self.root + '/tmp.txt', FileSystem)

    # def test_init_check_fail(self):
    #     try:
    #         fi.Directory(self.root + '/sub3', FileSystem, fi.FileFactory)
    #         self.fail("FileNotFoundOrWrongTypeError not thrown.")
    #     except fi.FileNotFoundOrWrongTypeError as e:
    #         assert True
