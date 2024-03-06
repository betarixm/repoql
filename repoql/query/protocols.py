from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, TypeVar

_T = TypeVar("_T")
_U = TypeVar("_U")


@dataclass
class GroupByResult(Generic[_T, _U]):
    underlying: Iterator[tuple[_U, Queryable[_T, _U]]]


Queryable = Iterator[_T] | GroupByResult[_T, _U]
