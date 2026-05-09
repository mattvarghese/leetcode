# 16 https://leetcode.com/problems/3sum-closest/description/

import pytest
from l00016_3sum_closest import Solution, Solution2


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # --- LeetCode Example 1 ---
        # [-1, 2, 1, -4], target 1 -> sum 2 ([-1, 2, 1])
        ([-1, 2, 1, -4], 1, 2),
        # --- LeetCode Example 2 ---
        ([0, 0, 0], 1, 0),
        # --- Exact Match ---
        ([1, 1, 1, 1], 3, 3),
        # --- Negative Numbers & Negative Target ---
        ([-10, -5, 0, 5, 10], -2, 0),  # (-5, 0, 5) is 0, closest to -2
        # --- Large Gaps ---
        ([1, 1, 15, 20, 25], 5, 17),  # (1, 1, 15) is 17
        # --- All values far from target ---
        ([10, 20, 30], 100, 60),
        # --- Boundary: Minimal Size ---
        ([1, 2, 3], 10, 6),
        # --- Duplicates that don't affect closest ---
        ([1, 1, 1, 0], -100, 2),
    ],
)
@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_three_sum_closest(sol, nums, target, expected):
    assert sol.threeSumClosest(nums, target) == expected
