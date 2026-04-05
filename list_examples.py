#!/usr/bin/env python3
"""Collection of Python list examples for learning and experimentation.

Run this file to see example outputs. Each section demonstrates
common list operations and idioms with short explanations.
"""

from copy import deepcopy


def basics():
    # creating lists
    a = []
    b = [1, 2, 3]
    c = list(range(5))  # [0,1,2,3,4]
    print("creation:", a, b, c)

    # indexing and negative indices
    print("indexing b[0], b[-1]:", b[0], b[-1])

    # slicing (start:stop:step)
    print("slice c[1:4]:", c[1:4])
    print("slice c[::-1] (reverse):", c[::-1])


def modify_methods():
    x = [1, 2, 3]
    x.append(4)  # add single element
    print("append:", x)

    x.extend([5, 6])  # extend with iterable
    print("extend:", x)

    x.insert(0, 0)  # insert at index
    print("insert at 0:", x)

    x.remove(2)  # remove first occurrence of value
    print("remove 2:", x)

    popped = x.pop()  # pop last
    print("pop():", popped, "->", x)

    # index, count
    print("index of 3:", x.index(3))
    print("count of 3:", x.count(3))

    # clear
    y = x.copy()
    y.clear()
    print("clear ->", y)


def sorting_and_reversing():
    vals = [3, 1, 4, 1, 5, 9]
    print("original:", vals)
    vals.sort()  # in-place sort
    print("sort():", vals)

    vals = [3, 1, 4, 1, 5, 9]
    sorted_copy = sorted(vals, reverse=True)  # returns new list
    print("sorted(..., reverse=True):", sorted_copy)

    vals.reverse()  # in-place reverse
    print("reverse():", vals)


def comprehensions_and_generators():
    nums = [0, 1, 2, 3, 4]
    squares = [n * n for n in nums]
    print("list comprehension (squares):", squares)

    # conditional comprehension
    evens = [n for n in nums if n % 2 == 0]
    print("evens:", evens)

    # nested comprehension (flattening)
    grid = [[r * 3 + c for c in range(3)] for r in range(3)]
    print("grid:", grid)


def conversion_and_join_split():
    words = ["hello", "world"]
    s = " ".join(words)
    print("join:", s)

    back = s.split()
    print("split:", back)


def unpacking_and_enum_zip():
    a, b, *rest = [1, 2, 3, 4]
    print("unpacking a,b,rest:", a, b, rest)

    for idx, val in enumerate(["a", "b", "c"], start=1):
        print("enumerate:", idx, val)

    letters = ["x", "y", "z"]
    numbers = [1, 2, 3]
    print("zip example:", list(zip(letters, numbers)))


def shallow_vs_deep_copy():
    orig = [[1, 2], [3, 4]]
    shallow = orig.copy()
    deep = deepcopy(orig)

    shallow[0].append(99)
    print("after modifying shallow[0]: orig=", orig, "shallow=", shallow, "deep=", deep)


def useful_patterns():
    # remove duplicates preserving order
    items = [3, 1, 2, 3, 2, 4]
    seen = set()
    unique = [x for x in items if not (x in seen or seen.add(x))]
    print("unique preserving order:", unique)

    # flatten nested list (one level)
    nested = [[1, 2], [3, 4], [5]]
    flat = [x for sub in nested for x in sub]
    print("flattened:", flat)


def functional_style():
    nums = [0, 1, 2, 3, 4]
    doubled = list(map(lambda x: x * 2, nums))
    filtered = list(filter(lambda x: x % 2 == 0, nums))
    print("map ->", doubled)
    print("filter ->", filtered)


def performance_notes():
    # for many appends, using list.append in a loop is OK; for many inserts at front, deque is better
    print("performance: use list.append for amortized O(1) append; use collections.deque for fast pops/inserts at ends")


def main():
    print("--- Basics ---")
    basics()
    print("\n--- Modify Methods ---")
    modify_methods()
    print("\n--- Sorting & Reversing ---")
    sorting_and_reversing()
    print("\n--- Comprehensions & Generators ---")
    comprehensions_and_generators()
    print("\n--- Join & Split ---")
    conversion_and_join_split()
    print("\n--- Unpacking, enumerate, zip ---")
    unpacking_and_enum_zip()
    print("\n--- Shallow vs Deep Copy ---")
    shallow_vs_deep_copy()
    print("\n--- Useful Patterns ---")
    useful_patterns()
    print("\n--- Functional Style ---")
    functional_style()
    print("\n--- Performance Notes ---")
    performance_notes()


if __name__ == "__main__":
    main()
