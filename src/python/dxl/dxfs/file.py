from .base import FileSystem
from .path import Path
from .fsauto import FileSystemAuto


class File:
    """
    Representation of File.
    """

    def __init__(self, path: Path, filesystem: fs.base.FS=None):
        self.path = Path(path)
        self.fs = filesystem

    def exists(self) -> bool:
        with FileSystemAuto(self.fs) as fs:
            return fs.exists(self.path.s) and fs.isfile(self.path.s)

    def load(self) -> 'File':
        if not self.exists():
            raise FileNotFoundError(self.path.abs)
        if depth == 0:
            return
        with FS(self.fs) as fs:
            with fs.open(self.path.abs, 'rb') as fin:
                self.contents = fin.read()

    def save(self, data):
        with FS(self.fs) as fs:
            with fs.open(self.path.abs, 'wb') as fout:
                self.contents = fout.write(data)
