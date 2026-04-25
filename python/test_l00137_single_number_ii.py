# https://leetcode.com/problems/single-number-ii/

import pytest
from l00137_single_number_ii import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        # --- LeetCode Official Examples ---
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),
        # --- Edge Cases & Constraints ---
        ([5], 5),  # Single element only
        ([-2, -2, 1, 1, 4, 1, -2], 4),  # Mixed with negatives
        ([-2, -2, -3, -2], -3),  # All negatives
        # --- Large Values ---
        ([2147483647, 2147483647, 2147483647, 10], 10),  # Max 32-bit Signed Int
    ],
)
def test_single_number_ii_logic(sol, nums, expected):
    """
    Verifies the bitmasking logic correctly identifies the unique element.
    """
    result = sol.singleNumber(nums)
    assert result == expected, (
        f"Failed for nums={nums}: expected {expected}, got {result}"
    )


def test_bitmask_integrity(sol):
    """
    Verify architectural integrity:
    Ensures that the state machine (ones/twos) correctly resets
    after three occurrences of the same number.
    """
    # 3 occurrences of 10, 3 occurrences of 20, 1 occurrence of 30
    nums = [10, 20, 30, 10, 20, 10, 20]
    assert sol.singleNumber(nums) == 30
