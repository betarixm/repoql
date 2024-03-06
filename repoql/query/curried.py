import functools
from typing import Any, Callable, TypeVar

from repoql.query import engine as Q
from repoql.query.protocols import Queryable
from repoql.query.typings import SupportsRichComparisonT

_T = TypeVar("_T")
_U = TypeVar("_U")

get = Q.get


def group_by(
    key: Callable[[_T], SupportsRichComparisonT],
) -> Callable[
    [Queryable[_T, SupportsRichComparisonT]], Queryable[_T, SupportsRichComparisonT]
]:
    return functools.partial(Q.group_by, key=key)


def map(function: Callable[[_T], _U]):
    return functools.partial(Q.map, function=function)


def reduce(
    function: Callable[[_U, _T], _U],
    initial: _U,
) -> Callable[[Queryable[_T, Any]], _U]:
    return functools.partial(Q.reduce, function=function, initial=initial)


def select(
    where: Callable[[_T], bool] = lambda _: True,
    limit: int | None = None,
) -> Callable[[Queryable[_T, Any]], Queryable[_T, Any]]:
    return functools.partial(Q.select, where=where, limit=limit)


def sorted(
    key: Callable[[_T], SupportsRichComparisonT],
) -> Callable[[Queryable[_T, Any]], Queryable[_T, Any]]:
    return functools.partial(Q.sorted, key=key)


ungroup = Q.ungroup


def unique(
    key: Callable[[_T], Any] = lambda _: _,
) -> Callable[[Queryable[_T, Any]], Queryable[_T, Any]]:
    return functools.partial(Q.unique, key=key)
