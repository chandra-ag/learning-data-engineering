#!/usr/bin/env python3
"""Dictionary examples for learning common patterns and methods."""

def basics():
    # creation
    a = {}
    b = dict(one=1, two=2)
    c = {"a": 1, "b": 2}
    print("creation:", a, b, c)

    # access with get and []
    print("b['one']:", b['one'])
    print("c.get('z', 'missing'):", c.get('z', 'missing'))


def update_and_merge():
    d1 = {"x": 1, "y": 2}
    d2 = {"y": 20, "z": 3}
    d1.update(d2)  # in-place merge (overwrites overlapping keys)
    print("update ->", d1)

    # using {**d1, **d2} creates a new merged dict (d2 wins on conflicts)
    merged = {**{"a": 1}, **{"b": 2}}
    print("merge new dict:", merged)


def iteration_and_items():
    d = {"a": 1, "b": 2}
    print("keys:", list(d.keys()))
    print("values:", list(d.values()))
    print("items:", list(d.items()))

    # iterate over key, value
    for k, v in d.items():
        print(f"item: {k} -> {v}")


def comprehensions():
    nums = [1, 2, 3]
    # dict comprehension: square mapping
    squares = {n: n * n for n in nums}
    print("comprehension:", squares)


def common_patterns():
    # invert a mapping (careful with non-unique values)
    d = {"a": 1, "b": 2, "c": 1}
    inv = {}
    for k, v in d.items():
        inv.setdefault(v, []).append(k)
    print("invert (group by value):", inv)

    # counting with dict
    s = "abracadabra"
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    print("counts:", counts)


def main():
    print("--- Dict Basics ---")
    basics()
    print("\n--- Update & Merge ---")
    update_and_merge()
    print("\n--- Iteration & Items ---")
    iteration_and_items()
    print("\n--- Comprehensions ---")
    comprehensions()
    print("\n--- Common Patterns ---")
    common_patterns()


if __name__ == "__main__":
    main()
