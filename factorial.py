#!/usr/bin/env python3
"""Simple factorial utility.

Usage:
  python factorial.py 5
  python factorial.py       # prompts for input
"""
import argparse
import sys

def factorial(n: int) -> int:
    """Return n! for non-negative integers.

    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute factorial of a non-negative integer.")
    parser.add_argument("n", type=int, nargs="?", help="non-negative integer (if omitted, will prompt)")
    args = parser.parse_args()

    if args.n is None:
        try:
            args.n = int(input("Enter a non-negative integer: ").strip())
        except Exception:
            print("Invalid input.", file=sys.stderr)
            sys.exit(1)

    try:
        print(factorial(args.n))
    except Exception as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
