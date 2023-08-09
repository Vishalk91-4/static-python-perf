#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
"""Simple, brute-force N-Queens solver."""
__author__ = "collinwinter@google.com (Collin Winter)"


# Pure-Python implementation of itertools.permutations().
def permutations(iterable, r=None):
    """permutations(range(3), 2) --> (0,1) (0,2) (1,0) (1,2) (2,0) (2,1)"""
    pool = tuple(iterable)
    n = len(pool)
    if r is None:
        r = n
    indices = list(range(n))
    cycles = list(range(n - r + 1, n + 1))[::-1]
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1 :] + indices[i : i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


# From http://code.activestate.com/recipes/576647/
def n_queens(queen_count):
    """N-Queens solver.

    Args:
        queen_count: the number of queens to solve for. This is also the
            board size.

    Yields:
        Solutions to the problem. Each yielded value is looks like
        (3, 8, 2, 1, 4, ..., 6) where each number is the column position for the
        queen, and the index into the tuple indicates the row.
    """
    cols = range(queen_count)
    for vec in permutations(cols):
        if (
            queen_count
            == len(set(vec[i] + i for i in cols))  # noqa: C401
            == len(set(vec[i] - i for i in cols))  # noqa: C401
        ):
            yield vec


def bench_n_queens(queen_count):
    return list(n_queens(queen_count))


def run():
    queen_count = 8
    bench_n_queens(queen_count)


if __name__ == "__main__":
    import sys

    num_iterations = 1
    if len(sys.argv) > 1:
        num_iterations = int(sys.argv[1])

    queen_count = 8
    for _ in range(num_iterations):
        res = bench_n_queens(queen_count)
        assert len(res) == 92
