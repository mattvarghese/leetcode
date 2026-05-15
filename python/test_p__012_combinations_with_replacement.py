import math

import pytest
from p__012_combinations_with_replacement import Combinations


@pytest.fixture
def solver():
    return Combinations()


@pytest.mark.parametrize(
    "iterable, r",
    [
        # --- 1. Project Euler #30 Case ---
        # 6 slots, 10 digits (0-9). Formula: c(10+6-1, 6) = 5005
        (range(10), 6),
        # --- 2. Small Standard Case ---
        # 2 items, 3 options. Formula: c(3+2-1, 2) = c(4, 2) = 6
        ([1, 2, 3], 2),
        # --- 3. Single Selection ---
        # 1 item, 5 options. Formula: c(5+1-1, 1) = 5
        (["A", "B", "C", "D", "E"], 1),
        # --- 4. Large r, Small n ---
        # 5 items, 2 options. Formula: c(2+5-1, 5) = c(6, 5) = 6
        ([0, 1], 5),
        # --- 5. Empty Case ---
        ([], 0),
        # --- 6. r is 0 ---
        # Choosing 0 items always results in 1 empty combination (tuple)
        ([1, 2, 3], 0),
    ],
)
def test_combinations_count(solver, iterable, r):
    """
    Verifies that the number of unique combinations generated matches
    the mathematical formula for combinations with replacement.
    Formula: (n + r - 1)! / (r!(n - 1)!)
    """
    pool = list(iterable)
    n = len(pool)

    # Calculate expected count using math.comb (Stars and Bars)
    if n == 0 and r > 0:
        expected_count = 0
    elif r == 0:
        expected_count = 1
    else:
        expected_count = math.comb(n + r - 1, r)

    # Generate all combinations and store in a set to verify uniqueness
    # Note: result must be a set of tuples because tuples are hashable
    results = set(solver.WithReplacement(pool, r))

    assert len(results) == expected_count


def test_lexicographical_order(solver):
    """
    Specifically checks that the logic produces sorted indices (lexicographical order)
    and doesn't include permutations.
    """
    iterable = [1, 2, 3]
    r = 2
    results = list(solver.WithReplacement(iterable, r))

    # Expected: (1,1), (1,2), (1,3), (2,2), (2,3), (3,3)
    # Permutations like (2,1) or (3,1) should NOT be present.
    assert (2, 1) not in results
    assert (1, 2) in results
    assert len(results) == 6
