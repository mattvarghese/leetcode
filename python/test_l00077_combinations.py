# https://leetcode.com/problems/combinations/

import pytest

# Assuming your file is named l00077_combinations.py
# Adjust the import name to match your actual filename
from l00077_combinations import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "n, k, expected",
    [
        # --- LeetCode Official Examples ---
        (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
        (1, 1, [[1]]),
        # --- Edge Cases & Constraints ---
        (4, 1, [[1], [2], [3], [4]]),  # k=1 (single elements)
        (4, 4, [[1, 2, 3, 4]]),  # k=n (only one combination)
        (
            5,
            3,
            [
                [1, 2, 3],
                [1, 2, 4],
                [1, 2, 5],
                [1, 3, 4],
                [1, 3, 5],
                [1, 4, 5],
                [2, 3, 4],
                [2, 3, 5],
                [2, 4, 5],
                [3, 4, 5],
            ],
        ),
        # n is larger, but k is small
        (3, 2, [[1, 2], [1, 3], [2, 3]]),
    ],
)
def test_combine_basic(sol, n, k, expected):
    """
    Verifies that the generated combinations match the expected list.
    We sort the outer and inner lists to ensure comparison doesn't fail
    due to order, though your backtracking naturally produces sorted results.
    """
    result = sol.combine(n, k)

    # Sort results for deterministic comparison
    actual_sorted = sorted([sorted(c) for c in result])
    expected_sorted = sorted([sorted(e) for e in expected])

    assert actual_sorted == expected_sorted, (
        f"Failed for n={n}, k={k}: expected {len(expected)} items, got {len(result)}"
    )


def test_combination_count(sol):
    """
    Mathematical verification: The number of combinations should be nCr.
    For n=5, k=2, 5C2 = 10.
    """
    import math

    n, k = 5, 2
    expected_count = math.comb(n, k)
    result = sol.combine(n, k)
    assert len(result) == expected_count


def test_combination_integrity(sol):
    """
    Verify architectural constraints of combinations:
    1. Each combination must have length k.
    2. All elements in a combination must be unique.
    3. All elements must be within the range [1, n].
    """
    n, k = 6, 3
    result = sol.combine(n, k)

    for combo in result:
        assert len(combo) == k
        assert len(set(combo)) == k  # Check for duplicates
        for val in combo:
            assert 1 <= val <= n
