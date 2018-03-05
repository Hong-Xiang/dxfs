import unittest
from fs.memoryfs import MemoryFS
from dxl.fs.directory import Directory, match_directory, match_file


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
        result = d.listdir()
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

    def test_list_only_matched_dirs(self):
        mfs = MemoryFS()
        mfs.touch('test.txt')
        for i in range(2):
            mfs.makedir('sub{}'.format(i))
        mfs.makedir('foo')
        d = Directory('.', mfs)
        result = (d.listdir_as_observable()
                  .filter(lambda o: isinstance(o, Directory))
                  .filter(lambda d: d.match(['sub*']))
                  .to_list().to_blocking().first())
        self.assertEqual(len(result), 2)
        for o in result:
            self.assertIsInstance(o, Directory)
        paths = [o.path.s for o in result]
        self.assertIn('sub0', paths)
        self.assertIn('sub1', paths)

    def test_copy_files(self):
        mfs = MemoryFS()
        mfs.touch('txt1.txt')
        mfs.touch('txt2.txt')
        mfs.makedir('sub1')
        mfs.makedir('sub2')
        new_files = ['sub1/txt1.txt', 'sub1/txt2.txt',
                     'sub2/txt1.txt', 'sub2/txt2.txt']
        for n in new_files:
            self.assertFalse(mfs.exists(n))
        d = Directory('.', mfs)
        targets = d.listdir_as_observable().filter(match_directory(['sub*']))
        sources = d.listdir_as_observable().filter(match_file(['txt*']))
        sources.subscribe(lambda f: print(f.path.s))
        sources_list = []
        sources.subscribe(sources_list.append)
        results = (targets.flat_map(lambda d: d.sync(sources))
                   .to_list()
                   .to_blocking()
                   .first())
        self.assertEqual(len(results), 4)
        for n in new_files:
            self.assertTrue(mfs.exists(n))

    def test_osfs(self):
        d = Directory('/some/random/paths')
        self.assertFalse(d.exists())
    
    def test_system_path(self):
        from fs.osfs import OSFS
        d = Directory('/tmp', OSFS('/'))
        self.assertEqual(d.system_path(), '/tmp')
