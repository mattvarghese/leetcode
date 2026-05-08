# 4 https://leetcode.com/problems/median-of-two-sorted-arrays/

import pytest
from l00004_median_of_two_sorted_arrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, expected_median",
    [
        # --- LeetCode Example 1 ---
        # Combined: [1, 2, 3], Median: 2.0
        ([1, 3], [2], 2.0),
        # --- LeetCode Example 2 ---
        # Combined: [1, 2, 3, 4], Median: (2+3)/2 = 2.5
        ([1, 2], [3, 4], 2.5),
        # --- One Empty Array ---
        ([], [1], 1.0),
        ([2, 3], [], 2.5),
        ([], [1, 2, 3, 4, 5], 3.0),
        # --- Single Elements ---
        ([1], [2], 1.5),
        ([2], [1], 1.5),
        # --- Different Lengths (Odd Total) ---
        # [1, 2, 3, 4, 5, 6, 7] -> 4.0
        ([1, 2], [3, 4, 5, 6, 7], 4.0),
        ([1, 5, 6], [2, 3, 4, 7], 4.0),
        # --- Different Lengths (Even Total) ---
        # [1, 2, 3, 4, 5, 6, 7, 8] -> (4+5)/2 = 4.5
        ([1, 2, 3, 4], [5, 6, 7, 8], 4.5),
        ([1, 8], [2, 3, 4, 5, 6, 7], 4.5),
        # --- Overlapping Values ---
        ([1, 3, 8, 9], [7, 11, 18, 19], 8.5),
        ([1, 1, 1], [1, 1, 1], 1.0),
        # --- Large Gaps ---
        ([1, 2], [10, 11], 6.0),
        ([10, 11], [1, 2], 6.0),
        # --- Mine ---
        ([6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5], 5.0),
        ([1, 2, 6, 8, 10], [0, 3, 4, 5, 7, 9], 5.0),
        ([1, 2, 6, 8, 10], [0, 3, 4, 5, 7, 9], 5.0),
    ],
)
def test_find_median_sorted_arrays(nums1, nums2, expected_median):
    sol = Solution()
    # Using pytest.approx for floating point comparisons
    assert pytest.approx(sol.findMedianSortedArrays(nums1, nums2)) == pytest.approx(
        expected_median
    )


def test_shorter_array_logic():
    """
    Ensures the code handles cases where the first array
    is significantly longer than the second.
    """
    sol = Solution()
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums2 = [5, 6]
    # Combined: [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10]
    # Middle elements are 5 and 6
    assert pytest.approx(sol.findMedianSortedArrays(nums1, nums2)) == 5.5
