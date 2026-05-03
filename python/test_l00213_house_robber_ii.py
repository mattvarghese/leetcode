# 213 https://leetcode.com/problems/house-robber-ii/

from typing import List

import pytest
from l00213_house_robber_ii import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        # --- LeetCode Original Cases ---
        ([2, 3, 2], 3),  # Rob house 2 (3). Cannot rob 1 & 3 because they are neighbors.
        ([1, 2, 3, 1], 4),  # Rob 1 & 3 (1+3=4) or 2 & 4 (2+1=3). Max is 4.
        ([1, 2, 3], 3),  # Max is house 3.
        # --- Edge Cases ---
        ([], 0),  # No houses
        ([10], 10),  # Single house (circularity doesn't apply)
        ([10, 20], 20),  # Two houses: they are neighbors, take the max.
        ([20, 10], 20),  # Two houses: they are neighbors, take the max.
        ([7, 7, 7, 7], 14),  # Even number of identical houses (rob 2)
        # --- Logic Drivers (The "Circular Trap") ---
        (
            [100, 1, 1, 100],
            101,
        ),  # Linear would be 200. Circular forces skipping one 100.
        (
            [1, 2, 1, 1, 100],
            102,
        ),  # Your previous case: (2+100) or (1+1+100) is now limited.
        ([200, 3, 140, 20, 10], 340),  # Rob 200 and 140.
        (
            [1, 3, 1, 3, 100],
            103,
        ),  # Testing if skipping the last allows better previous rob.
        # --- Large Gap Logic ---
        ([1, 10, 1, 1, 10, 1], 20),  # Skip first/last to get the two 10s in the middle.
    ],
)
def test_house_robber(sol, nums: List[int], expected: int):
    observed = sol.rob(nums)
    assert observed == expected, (
        f"Failed for nums={nums}. Expected {expected}, but got {observed}"
    )
