# 15 https://leetcode.com/problems/3sum/


import pytest
from l00015_3sum import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        # --- LeetCode Example 1 ---
        # Duplicates handled: [-1, -1, 2] and [-1, 0, 1]
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        # --- LeetCode Example 2 ---
        ([0, 1, 1], []),
        # --- LeetCode Example 3 ---
        ([0, 0, 0], [[0, 0, 0]]),
        # --- No possible triplets ---
        ([1, 2, -2, -1], []),
        # --- Boundary: Minimal array size ---
        ([-1, 0, 1], [[-1, 0, 1]]),
        # --- Multiple duplicates ---
        # Should only return one [0,0,0]
        ([0, 0, 0, 0], [[0, 0, 0]]),
        # --- Pruning: All positive ---
        ([1, 2, 3, 4, 5], []),
        # --- Pruning: All negative ---
        ([-5, -4, -3, -2, -1], []),
        # --- Large gaps with duplicates ---
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        # --- Complex duplicates ---
        ([-2, -2, -2, 0, 2, 2, 2], [[-2, 0, 2]]),
        # --- Mixed values including duplicate triplets ---
        (
            [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],
            [
                [-4, 0, 4],
                [-4, 1, 3],
                [-3, -1, 4],
                [-3, 0, 3],
                [-3, 1, 2],
                [-2, -1, 3],
                [-2, 0, 2],
                [-1, -1, 2],
                [-1, 0, 1],
            ],
        ),
    ],
)
def test_three_sum(nums, expected):
    sol = Solution()
    result = sol.threeSum(nums)

    # Since the order of triplets and elements doesn't matter for correctness,
    # we sort both the results and expected values for comparison.
    actual_sorted = sorted([sorted(t) for t in result])
    expected_sorted = sorted([sorted(t) for t in expected])

    assert actual_sorted == expected_sorted


def test_large_input_performance():
    """
    Ensures that the O(n^2) approach handles a moderately large input
    without exponential explosion due to duplicates.
    """
    sol = Solution()
    # 500 zeros
    nums = [0] * 500
    assert sol.threeSum(nums) == [[0, 0, 0]]


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Standard case
        ([3, 1, 4, 1, 5, 9, 2, 6, 5], [1, 1, 2, 3, 4, 5, 5, 6, 9]),
        # Already sorted
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        # Reverse sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        # Empty array
        ([], []),
        # Single element
        ([1], [1]),
        # Two elements (swapped)
        ([2, 1], [1, 2]),
        # All same elements
        ([0, 0, 0], [0, 0, 0]),
        # Negative numbers
        ([-1, -5, 10, 7, 0], [-5, -1, 0, 7, 10]),
        # Large range of values
        ([100, -100, 50, -50, 0], [-100, -50, 0, 50, 100]),
    ],
)
def test_merge_sort(nums, expected):
    sol = Solution()
    # Create a copy so we don't mutate the parametrized input directly
    nums_to_sort = list(nums)

    if not nums_to_sort:
        # Edge case for empty list
        sol.mergeSort(nums_to_sort, 0, 0)
    else:
        # Call with start=0 and end=len(nums)-1 for inclusive logic
        sol.mergeSort(nums_to_sort, 0, len(nums_to_sort) - 1)

    assert nums_to_sort == expected


def test_merge_sort_random():
    import random

    sol = Solution()
    # Generate 1000 random numbers
    nums = [random.randint(-1000, 1000) for _ in range(1000)]
    expected = sorted(nums)

    sol.mergeSort(nums, 0, len(nums) - 1)
    assert nums == expected
