import os
import sys

import pytest

# Add the current directory to sys.path so pytest can find the module
sys.path.append(os.path.dirname(__file__))

from l00046_permutations import solve


@pytest.mark.parametrize("func", [solve])
@pytest.mark.parametrize(
    "nums, expected_count",
    [
        # --- LeetCode Official Examples ---
        ([1, 2, 3], 6),  # Example 1: 3! = 6 permutations
        ([0, 1], 2),  # Example 2: 2! = 2 permutations
        ([1], 1),  # Example 3: 1! = 1 permutation
        # --- Additional Edge Cases & Constraints ---
        ([-1, 0, 1], 6),  # Negative numbers (constraint: -10 <= nums[i] <= 10)
        ([], 0),  # Empty list: Should return [] or [[]] based on implementation
        ([10, -10], 2),  # Boundary values
        ([5, 4, 3, 2, 1], 120),  # Larger set (5! = 120) to check performance
    ],
)
def test_permutations_coverage(func, nums, expected_count):
    # Handle the empty list edge case explicitly if your 'solve' returns []
    if not nums:
        result = func(nums)
        # Permutations of empty set is often considered one empty list [[]]
        # or simply []. Check your solve logic for consistency.
        assert len(result) <= 1
        return

    result = func(nums)

    # 1. Verify the total number of permutations (N!)
    assert len(result) == expected_count, (
        f"{func.__name__} failed for {nums}: expected {expected_count} results, got {len(result)}"
    )

    # 2. Verify all permutations are unique
    # We convert sub-lists to tuples to make them hashable for a set
    unique_results = {tuple(p) for p in result}
    assert len(unique_results) == expected_count, (
        f"{func.__name__} for {nums} contains duplicate permutations"
    )

    # 3. Verify each permutation contains exactly the same original elements
    expected_sorted = sorted(nums)
    for p in result:
        assert len(p) == len(nums), f"Permutation {p} length mismatch"
        assert sorted(p) == expected_sorted, (
            f"Permutation {p} corrupted original values"
        )


def test_exact_output_match():
    """Verify an exact match for LeetCode Example 2 to ensure list-of-lists structure."""
    nums = [0, 1]
    expected = [[0, 1], [1, 0]]
    result = solve(nums)

    # Sort both the outer list and inner lists to compare equality regardless of order
    assert sorted([sorted(p) for p in result]) == sorted([sorted(p) for p in expected])
