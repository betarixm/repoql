from pathlib import Path

from pygit2 import Repository


def use_repository(repository_or_path: Repository | str | Path) -> Repository:
    match repository_or_path:
        case Repository():
            return repository_or_path
        case _:
            return Repository(str(repository_or_path))
