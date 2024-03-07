from typing import Callable

from pygit2 import Commit, Oid, Repository


def commit_by_object_id(repository: Repository) -> Callable[[Oid], Commit]:
    return lambda object_id: repository.revparse_single(object_id.hex).peel(1)
