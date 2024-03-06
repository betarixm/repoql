# RepoQL

> A Python library designed for querying git repositories

RepoQL is a Python library designed for querying git repositories. It provides a minimalistic interface wrapping around [`pygit2`](https://www.pygit2.org/), allowing you to perform various queries on git repositories.

## Features

- Provides functional programming style for querying git repositories.
- Fully type hinted for improved code readability and maintainability.
- Minimalistic design focused on simplicity and ease of use.

## Usage

```py
from pathlib import Path
from typing import Any, Callable, Iterator

from pygit2 import Repository

from repoql import BlobRelation
from repoql import Query as Q
from repoql import Queryable, blob_relation, compose

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


repo = Repository("[path to your git repository]")

result = blobs_by_relative_path(Path(".gitignore"))(blob_relation.from_repository(repo))
```

Check out `repoql/recipes.py` for more examples.

## Disclaimer

RepoQL is provided as-is and without warranty. Please note that RepoQL is not intended for production use as it is not battle-tested. It's best suited for experimental or educational purposes. Use it at your own risk.
