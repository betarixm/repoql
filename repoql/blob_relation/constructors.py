import logging
from itertools import chain
from pathlib import Path
from typing import Iterator

from pygit2 import Blob, Commit, Object, Repository, Tree

from repoql.blob_relation.models import BlobRelation


def from_repository(
    repository: Repository,
):
    return from_objects(
        iter(repository.walk(repository.head.target)),
    )


def from_objects(
    objects: Iterator[Object],
) -> Iterator[BlobRelation]:
    return chain.from_iterable(map(from_object, objects))


def from_object(
    object: Object,
    path: Path = Path(),
    last_commit: Commit | None = None,
) -> Iterator[BlobRelation]:
    match object:
        case Blob():
            assert object.name is not None
            assert last_commit is not None

            yield from_blob(object, last_commit, path / object.name)
        case Commit():
            try:
                yield from from_object(object.tree, path=path, last_commit=object)
            except KeyError as e:
                logging.warning(e)  # FIXME
        case Tree(name=child):

            def inner(object: Object) -> Iterator[BlobRelation]:
                yield from from_object(
                    object, path=path / (child or ""), last_commit=last_commit
                )

            yield from chain.from_iterable(map(inner, iter(object)))

        case _:
            assert False, "Unreachable"


def from_blob(blob: Blob, commit: Commit, path: Path) -> BlobRelation:
    return BlobRelation(
        id=blob.id,
        path=path,
        commit=commit,
    )
