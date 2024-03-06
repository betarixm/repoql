from pathlib import Path
from typing import Any, Callable, Iterator

from repoql import BlobRelation
from repoql import Query as Q
from repoql import Queryable, compose
from repoql.hooks import use_pinned_iterable

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
