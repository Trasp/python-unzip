#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Unittests for the unzip function."""

__author__ = "Trasp"
__copyright__ = "Copyright (C) 2020 Trasp"
__license__ = "0BSD"

from unittest import TestCase
from collections import deque

from .unzip import unzip


def test_unzip_legacy() -> None:
    """Less widely used test convention."""
    from collections import deque
    assert unzip(zip(["a","b","c"], [1,2,3])) == (["a","b","c"], [1,2,3])
    assert unzip([("a",1), ("b",2), ("c",3)]) == (["a","b","c"], [1,2,3])
    assert unzip([("a",), ("b",), ("c",)]) == (["a", "b", "c"],)
    assert unzip(zip(["a"], [1])) == (["a"], [1])
    assert unzip([], tuple, list) == []
    assert unzip([("a", 1)], deque, list) == [deque(["a"]), deque([1])]
    assert unzip((["a"], ["b"]), lambda i: deque(i, 1)) == (deque(["b"]),)


class UnzipTests(TestCase):

    """Simple test unit for the unzip function."""

    def test_unzip(self) -> None:
        """Basic tests."""

        # Reverse zip objects and unpack other zip like iterables.
        i = ("a", 1), ("b", 2), ("c", 3)
        r = ["a", "b", "c"], [1, 2, 3]
        self.assertEqual(unzip(i), r, r)
        
        # Reverse zip objects and unpack other zip/generator like iterables.
        i = zip(["a", "b"], [1, 2])
        r = ["a", "b"], [1, 2]
        self.assertEqual(unzip(i), r, r)
        
        # Test that an empty collection is returned on StopIteration (no input)
        self.assertEqual(unzip([], list, tuple), ())

    def test_unzip_legacy(self) -> None:
        """Inlude a few tests written for lesser used test convention."""
        self.assertIsNone(test_unzip_legacy())

    def test_unzip_types(self) -> None:
        """Test container factory replacement."""
        output = unzip([("a", 1)], deque, list)
        self.assertEqual(output, [deque(["a"]), deque([1])])
        self.assertTrue(isinstance(output, list))
        self.assertTrue(isinstance(next(iter(output)), deque))


__all__ = ["UnzipTests"]

