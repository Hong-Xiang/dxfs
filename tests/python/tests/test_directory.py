import unittest
from fs.memoryfs import MemoryFS
from dxl.fs.directory import Directory


class TestDirectory(unittest.TestCase):
    def test_exist(self):
        mfs = MemoryFS()
        mfs.makedir('test')
        d = Directory('test', mfs)
        self.assertTrue(d.exists())
    

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
