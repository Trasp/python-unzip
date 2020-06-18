#!/bin/python3
# -*- coding: utf-8 -*-

"""Zip function in reverse."""

__author__ = "Stefan Asplund"
__copyright__ = "Copyright (C) 2020 Stefan Asplund"
__license__ = "0BSD"
__version__ = "1.0"

from typing import Iterable, Callable

ContainerFactory = Callable[[], Iterable]


def unzip(items: Iterable[Iterable],
            cls: ContainerFactory = list,
           ocls: ContainerFactory = tuple) -> Iterable:
    r"""Zip function in reverse.

    :param items: Zipped-like iterable.
    :type  items: iterable

    :param cls: Container factory. Callable that returns iterable containers,
        with a callable append attribute, to store the unzipped items. Defaults
        to ``list``.
    :type  cls: callable, optional

    :param ocls: Outer container factory. Callable that returns iterable
        containers. with a callable append attribute, to store the inner
        containers (see ``cls``). Defaults to ``tuple``.
    :type  ocls: callable, optional

    :returns: Unzipped items in instances returned from ``cls``, in an instance
        returned from ``main_cls``.

    """

    # iter() will return the same iterator passed to it whenever possible.
    items = iter(items)

    try:
        i = next(items)
    except StopIteration:
        return ocls()

    unzipped = ocls(cls([v]) for v in i)

    for i in items:
        for c, v in zip(unzipped, i):
            c.append(v)

    return unzipped


__all__ = [ "unzip" ]
