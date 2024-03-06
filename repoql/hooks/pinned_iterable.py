import itertools
from typing import Callable, Iterable, Iterator, TypeVar

_T = TypeVar("_T")


def use_pinned_iterable(underlying: Iterable[_T]) -> Callable[[], Iterator[_T]]:
    def pin():
        nonlocal underlying
        (
            duplicated,
            underlying,
        ) = itertools.tee(underlying, 2)

        return duplicated

    return pin
