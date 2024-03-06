from __future__ import annotations

import builtins
import functools
from itertools import chain, groupby
from typing import Any, Callable, Iterable, Iterator, TypeVar, cast

from repoql.query.protocols import GroupByResult, Queryable
from repoql.query.typings import SupportsRichComparisonT

_T = TypeVar("_T")
_U = TypeVar("_U")

_R = _T | tuple[_U, Iterator["_R"]]


def get(
    source: Queryable[_T, _U]
) -> Iterator[_T] | Iterable[tuple[_U, Iterator[_R[_U, _T]]]]:
    match source:
        case GroupByResult(underlying):

            return builtins.map(
                lambda pair: (pair[0], cast(Iterator[_R[_U, _T]], get(pair[1]))),
                underlying,
            )
        case _:
            return source


def select(
    source: Queryable[_T, Any],
    where: Callable[[_T], bool] = lambda _: True,
    limit: int | None = None,
) -> Queryable[_T, Any]:
    match source:
        case GroupByResult(underlying):
            return GroupByResult(
                underlying=builtins.map(
                    lambda group: (
                        group[0],
                        select(group[1], where=where, limit=limit),
                    ),
                    underlying,
                ),
            )
        case _:
            return _select(source=source, where=where, limit=limit)


def group_by(
    source: Queryable[_T, SupportsRichComparisonT],
    key: Callable[[_T], SupportsRichComparisonT],
) -> Queryable[_T, SupportsRichComparisonT]:
    match source:
        case GroupByResult(underlying):
            return GroupByResult(
                underlying=builtins.map(
                    lambda group: (group[0], group_by(group[1], key=key)),
                    underlying,
                ),
            )
        case _:
            return GroupByResult(
                underlying=groupby(builtins.sorted(source, key=key), key=key),
            )


def reduce(
    source: Queryable[_T, Any],
    function: Callable[[_U, _T], _U],
    initial: _U,
) -> _U:
    match source:
        case GroupByResult(underlying):
            return functools.reduce(
                lambda acc, group: reduce(group[1], function, acc),
                underlying,
                initial,
            )
        case _:
            return functools.reduce(function, source, initial)


def map(
    source: Queryable[_T, Any],
    function: Callable[[_T], _U],
) -> Queryable[_U, Any]:
    match source:
        case GroupByResult(underlying):
            return GroupByResult(
                underlying=builtins.map(
                    lambda group: (group[0], map(group[1], function)),
                    underlying,
                ),
            )
        case _:
            return builtins.map(function, source)


def sorted(
    source: Queryable[_T, Any],
    key: Callable[[_T], Any],
    reverse: bool = False,
) -> Queryable[_T, Any]:
    match source:
        case GroupByResult(underlying):
            return GroupByResult(
                underlying=builtins.map(
                    lambda group: (
                        group[0],
                        sorted(group[1], key=key, reverse=reverse),
                    ),
                    underlying,
                ),
            )
        case _:
            return iter(builtins.sorted(source, key=key, reverse=reverse))


def ungroup(source: Queryable[_T, _U]) -> Iterator[_T]:
    match source:
        case GroupByResult(underlying):
            return chain.from_iterable(
                builtins.map(lambda group: ungroup(group[1]), underlying)
            )
        case _:
            return source


def unique(source: Queryable[_T, Any], key: Callable[[_T], Any]) -> Queryable[_T, Any]:
    match source:
        case GroupByResult(underlying):
            return GroupByResult(
                underlying=builtins.map(
                    lambda group: (group[0], unique(group[1], key=key)),
                    underlying,
                ),
            )
        case _:
            return ungroup(select(group_by(source, key=key), limit=1))


def _select(
    source: Iterator[_T],
    where: Callable[[_T], bool] = lambda _: True,
    limit: int | None = None,
) -> Iterator[_T]:
    match limit, next(source, None):
        case 0, _:
            pass
        case _, None:
            pass
        case _, item:
            match where(item):
                case True:
                    yield item
                    found = True
                case False:
                    found = False
            yield from _select(source, where, limit - found if limit else None)
