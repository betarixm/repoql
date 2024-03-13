import logging
from itertools import chain
from pathlib import Path
from typing import Any, Callable, Iterator

from pygit2 import Blame, BlameHunk, Blob, Commit, Object, Oid, Repository, Tree

from repoql.blob_relation.models import BlobRelation
from repoql.fp import compose, pipe
from repoql.query import Query as Q
from repoql.query import Queryable


def from_path_and_commit_ids(
    path: Path, commit_ids: list[str], repository: Repository
) -> Iterator[BlobRelation]:
    commits = map(
        lambda x: repository.revparse_single(x).peel(1),
        commit_ids,
    )

    return (
        _
        for _ in map(
            lambda commit: _from_commit_and_path_silently(commit, path),
            commits,
        )
        if _ is not None
    )


def _from_commit_and_path_silently(
    commit: Commit,
    path: Path,
):
    try:
        return from_commit_and_path(commit, path)
    except KeyError as e:
        logging.warning(e)  # FIXME
        return None


def from_commit_and_path(
    commit: Commit,
    path: Path,
):

    return from_blob(
        _blob_by_path_in_commit(path, commit),
        commit,
        path,
    )


def from_blame(
    blame: Blame, commit_by_object_id: Callable[[Oid], Commit]
) -> Iterator[BlobRelation]:
    return pipe(
        map(lambda hunk: from_hunk(hunk, commit_by_object_id), blame),
        Q.unique(lambda blob: blob.id),
        Q.ungroup,
    )


def from_hunk(
    hunk: BlameHunk, commit_by_object_id: Callable[[Oid], Commit]
) -> BlobRelation:
    assert hunk.orig_path is not None

    return _blob_relation_by_path_in_commit(
        Path(hunk.orig_path), commit_by_object_id(hunk.orig_commit_id)
    )


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


def _blob_by_path(
    path: Path | str,
) -> Callable[[Queryable[BlobRelation, Any]], Iterator[BlobRelation]]:
    return compose(
        Q.select(where=lambda blob: str(blob.path) == str(path), limit=1),
        Q.ungroup,
    )


def _blob_relation_by_path_in_commit(path: Path | str, commit: Commit):
    return next(_blob_by_path(path)(from_object(commit)))


def _blob_by_path_in_commit(path: Path, commit: Commit):
    return commit.tree[str(path)].peel(3)
