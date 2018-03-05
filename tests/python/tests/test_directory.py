import unittest
from dxl.fs.directory import Directory


class TestDirectory(unittest.TestCase):
    def test_check_pos(self):
        assert fi.Directory.check(self.root + '/sub1', FileSystem)

    def test_check_pos_deffac(self):
        assert fi.Directory.check(self.root + '/sub1', FileSystem)

    def test_check_neg(self):
        assert not fi.Directory.check(self.root + '/tmp.txt', FileSystem)

    def test_init_check_fail(self):
        try:
            fi.Directory(self.root + '/sub3', FileSystem, fi.FileFactory)
            self.fail("FileNotFoundOrWrongTypeError not thrown.")
        except fi.FileNotFoundOrWrongTypeError as e:
            assert True
