#!/usr/bin/env python3
"""Set examples showing creation, operations, and use-cases."""


def basics():
    a = set()
    b = {1, 2, 3}
    c = set([2, 3, 4])
    print("creation:", a, b, c)

    # membership
    print("2 in b:", 2 in b)


def operations():
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    print("union:", s1 | s2)
    print("intersection:", s1 & s2)
    print("difference s1 - s2:", s1 - s2)
    print("symmetric difference:", s1 ^ s2)


def mutating_methods():
    s = {1, 2}
    s.add(3)
    print("add ->", s)
    s.discard(2)
    print("discard ->", s)
    s.update([4, 5])
    print("update ->", s)


def comprehensions_and_frozenset():
    squares = {x * x for x in range(6)}
    print("set comprehension:", squares)

    frozen = frozenset([1, 2, 3])
    print("frozenset (immutable):", frozen)


def use_cases():
    # remove duplicates
    items = [1, 2, 2, 3, 3, 3]
    unique = list(dict.fromkeys(items))  # preserves order
    print("unique preserving order (via dict):", unique)

    # or unordered
    print("unique via set (unordered):", list(set(items)))


def main():
    print("--- Set Basics ---")
    basics()
    print("\n--- Operations ---")
    operations()
    print("\n--- Mutating Methods ---")
    mutating_methods()
    print("\n--- Comprehensions & frozenset ---")
    comprehensions_and_frozenset()
    print("\n--- Use Cases ---")
    use_cases()


if __name__ == "__main__":
    main()
