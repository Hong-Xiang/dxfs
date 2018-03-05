from .base import ObjectOnFileSystem, FileSystem
from .path import Path
import fs
from .conf import mc


class File(ObjectOnFileSystem):
    """
    Representation of File.
    """

    def __init__(self, path: Path, filesystem: FileSystem=None):
        super().__init__(filesystem, path)

    def name(self):
        return self.path.n

    def suffix(self):
        return self.path.suffix

    def load(self) -> 'File':
        """
        Returns:

        - contents loaded by assuming file as binary str.
        """
        if not self.exists():
            raise FileNotFoundError(self.path.abs)
        with self.filesystem.open() as fs:
            with fs.open(self.path.s, 'rb') as fin:
                return fin.read()

    def save(self, data: str):
        with self.filesystem.open() as fs:
            with fs.open(self.path.s, 'wb') as fout:
                return fout.write(data)
