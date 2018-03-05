from .path import Path
from .base import ObjectOnFileSystem
from rx import Observable


class Directory(ObjectOnFileSystem):
    def __init__(self, path: Path, filesystem=None):
        super().__init__(filesystem, path)

    def listdir(self):
        with self.filesystem.open() as fs:
            children = fs.listdir()
        paths = [self.path / c for c in children]
        return rx.Observable.from_(paths)
