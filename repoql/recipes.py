from pathlib import Path
from typing import Any, Callable, Iterator

from pygit2 import Repository

from repoql import BlobRelation
from repoql import Query as Q
from repoql import Queryable, blob_relation, compose
from repoql.hooks import use_pinned_iterable
from repoql.utils.git import commit_by_object_id

blobs_by_relative_path: Callable[
    [Path], Callable[[Queryable[BlobRelation, Any]], Iterator[BlobRelation]]
] = lambda path: compose(
    Q.select(
        where=lambda blob: str(blob.path) == str(path),
        limit=None,
    ),
    Q.group_by(
        key=lambda blob: blob.id,
    ),
    Q.sorted(key=lambda blob: blob.commit.commit_time),
    Q.select(limit=1),
    Q.ungroup,
)

unique_paths: Callable[[Queryable[BlobRelation, Any]], Iterator[Path]] = compose(
    Q.unique(key=lambda blob: blob.path),
    Q.ungroup,
    lambda blobs: (blob.path for blob in blobs),
)


def blobs_by_unique_paths(
    blobs: Queryable[BlobRelation, Any]
) -> Iterator[Iterator[BlobRelation]]:
    assert isinstance(blobs, Iterator), "blobs must be an iterator here"

    pinned_blobs = use_pinned_iterable(blobs)

    return map(
        lambda path: blobs_by_relative_path(path)(pinned_blobs()),
        unique_paths(pinned_blobs()),
    )


def trajectories_of_active_files(
    repository: Repository,
) -> Iterator[Iterator[BlobRelation]]:
    blobs_on_head = blob_relation.from_object(repository.head.peel(1))

    paths = map(str, unique_paths(blobs_on_head))

    blames = map(repository.blame, paths)

    return map(
        lambda blame: blob_relation.from_blame(blame, commit_by_object_id(repository)),
        blames,
    )
