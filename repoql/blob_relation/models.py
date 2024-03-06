from dataclasses import dataclass
from pathlib import Path

from pygit2 import Commit, Oid


@dataclass
class BlobRelation:
    id: Oid
    path: Path
    commit: Commit
