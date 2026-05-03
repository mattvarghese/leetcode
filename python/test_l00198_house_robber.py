# 198 https://leetcode.com/problems/house-robber/

from typing import List

import pytest
from l00198_house_robber import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        # --- LeetCode Original Cases ---
        ([1, 2, 3, 1], 4),  # Example 1: Rob 1 and 3 (1+3=4)
        ([2, 7, 9, 3, 1], 12),  # Example 2: Rob 1, 3, and 5 (2+9+1=12)
        # --- Edge Cases ---
        ([], 0),  # No houses
        ([10], 10),  # Single house
        ([10, 20], 20),  # Two houses, take the max
        ([20, 10], 20),  # Two houses, take the max (first house)
        # --- Logic Drivers ---
        ([1, 1, 1], 2),  # Alternating 1s
        ([2, 1, 1, 2], 4),  # Large ends, small middle (2+2=4)
        ([1, 100, 1], 100),  # Massive middle house
        ([1, 2, 1, 1, 100], 102),  # Testing long-term DP accumulation
        ([0, 0, 0, 0], 0),  # All zeros
        ([1, 2, 3, 4, 5, 6, 7, 8], 20),  # Sequential accumulation
    ],
)
def test_house_robber(sol, nums: List[int], expected: int):
    observed = sol.rob(nums)
    assert observed == expected, (
        f"Failed for nums={nums}. Expected {expected}, but got {observed}"
    )
