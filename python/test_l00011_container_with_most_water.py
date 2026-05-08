# 11 https://leetcode.com/problems/container-with-most-water/description/


import pytest
from l00011_container_with_most_water import Solution


@pytest.mark.parametrize(
    "height, expected_area",
    [
        # --- LeetCode Example 1 ---
        # The lines are [1,8,6,2,5,4,8,3,7].
        # The max area is between index 1 (height 8) and index 8 (height 7).
        # Width = 8 - 1 = 7, Height = min(8, 7) = 7. Area = 7 * 7 = 49.
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        # --- LeetCode Example 2 ---
        ([1, 1], 1),
        # --- Minimal Case ---
        # Smallest possible array size per constraints
        ([4, 3], 3),
        # --- Wide and Short vs. Narrow and Tall ---
        # Wide: (index 0 to 4), width 4, height 2 -> 8
        # Tall: (index 1 to 2), width 1, height 10 -> 10
        ([2, 10, 10, 1, 2], 10),
        # --- Descending Heights ---
        # --- Descending Heights ---
        # (index 0, h=5) and (index 2, h=3) -> width 2, area 6
        ([5, 4, 3, 2, 1], 6),
        # --- Ascending Heights ---
        # (index 2, h=3) and (index 4, h=5) -> width 2, area 6
        ([1, 2, 3, 4, 5], 6),
        # --- "Valley" Pattern ---
        # Large walls at the ends, small in middle
        ([10, 1, 1, 1, 10], 40),
        # --- "Mountain" Pattern ---
        # Small walls at the ends, large in middle
        ([1, 10, 10, 1], 10),
        # --- All Heights Equal ---
        ([5, 5, 5, 5, 5], 20),
        # --- Large Gaps with Small Heights ---
        ([1, 2, 1], 2),
    ],
)
def test_max_area(height, expected_area):
    sol = Solution()
    assert sol.maxArea(height) == expected_area


def test_large_input_performance():
    """
    Ensures the O(n) two-pointer approach handles large arrays
    without timing out.
    """
    sol = Solution()
    # 10,000 elements of height 100
    height = [100] * 10000
    # Width = 9999, Height = 100. Area = 999,900
    assert sol.maxArea(height) == 999900
