#!/usr/bin/env python3
"""Tuple examples demonstrating immutability, packing/unpacking, and common idioms."""

from collections import namedtuple


def basics():
    t = (1, 2, 3)
    single = (1,)  # single-element tuple needs trailing comma
    empty = ()
    print("creation:", t, single, empty)

    # indexing
    print("t[0], t[-1]:", t[0], t[-1])


def packing_unpacking():
    a, b, c = (10, 20, 30)  # unpacking
    print("unpacked:", a, b, c)

    head, *middle, tail = [1, 2, 3, 4]
    print("head, middle, tail:", head, middle, tail)


def immutability_and_methods():
    t = (1, 2, 2, 3)
    print("count of 2:", t.count(2))
    print("index of 3:", t.index(3))

    # tuples are immutable; create new tuple to 'modify'
    t2 = t + (4,)
    print("concat ->", t2)


def namedtuple_example():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print("namedtuple:", p, 'x=', p.x, 'y=', p.y)


def main():
    print("--- Tuple Basics ---")
    basics()
    print("\n--- Packing & Unpacking ---")
    packing_unpacking()
    print("\n--- Immutability & Methods ---")
    immutability_and_methods()
    print("\n--- Namedtuple ---")
    namedtuple_example()


if __name__ == "__main__":
    main()
