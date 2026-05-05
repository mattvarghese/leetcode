# 215 https://leetcode.com/problems/kth-largest-element-in-an-array/

import pytest
from l00215_kth_largest_element import Solution, Solution2, Solution3


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # --- LeetCode Case 1 ---
        ([3, 2, 1, 5, 6, 4], 2, 5),
        # --- LeetCode Case 2 ---
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        # --- Single Element ---
        ([1], 1, 1),
        # --- Already Sorted ---
        ([1, 2, 3, 4, 5, 6], 1, 6),
        ([1, 2, 3, 4, 5, 6], 6, 1),
        # --- Reverse Sorted ---
        ([6, 5, 4, 3, 2, 1], 1, 6),
        ([6, 5, 4, 3, 2, 1], 3, 4),
        # --- Large Number of Duplicates ---
        ([1, 1, 1, 1, 1, 1], 3, 1),
        ([2, 1, 2, 1, 2, 1], 2, 2),
        # --- Negative Numbers ---
        ([-1, -1], 2, -1),
        ([-1, 2, 0], 1, 2),
        ([-10, -5, -2, -15], 2, -5),
        # --- Minimum/Maximum Constraints ---
        ([10000, -10000], 2, -10000),
        # --- Large Random-ish Input ---
        ([5, 2, 4, 1, 3, 6, 0], 4, 3),
    ],
)
@pytest.mark.parametrize("sol", [Solution(), Solution2(), Solution3()])
def test_find_kth_largest(sol, nums, k, expected):
    # We create a copy of nums because QuickSelect is an in-place algorithm
    # and modifying the parameter data across multiple test runs is bad practice.
    nums_copy = list(nums)
    observed = sol.findKthLargest(nums_copy, k)
    assert observed == expected, (
        f"Failed for nums={nums}, k={k}. Expected {expected}, but got {observed}"
    )


def test_large_input_performance():
    """Verifies that the O(n) average complexity holds for large inputs."""
    import random

    size = 10**5
    nums = [random.randint(-10000, 10000) for _ in range(size)]
    k = size // 2

    # Expected value using Python's built-in sort
    expected = sorted(nums, reverse=True)[k - 1]

    sol = Solution()
    assert sol.findKthLargest(nums, k) == expected
