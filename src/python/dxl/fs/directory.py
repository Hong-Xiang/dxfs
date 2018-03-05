from .path import Path
from .base import ObjectOnFileSystem
from .file import File
import rx


class Directory(ObjectOnFileSystem):
    def __init__(self, path: Path, filesystem=None):
        super().__init__(filesystem, path)

    def exists(self):
        result = super().exists()
        if not result:
            return result
        with self.filesystem.open() as fs:
            if not fs.isdir(self.path.s):
                raise NotADirectoryError(self.path.s)
        return result

    def listdir(self):
        with self.filesystem.open() as fs:
            children = fs.listdir(self.path.s)
            paths = [self.path / c for c in children]
            results = []
            for p in paths:
                print('paths', p.s)
                print(p)
                print('inner', fs.isfile('test_file.txt'))
                print(fs.isfile(p.s))
                if fs.isfile(p.s):
                    results.append(File(p, self.filesystem))
                else:
                    results.append(Directory(p, self.filesystem))
        return rx.Observable.from_(results)
