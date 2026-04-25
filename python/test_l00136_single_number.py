# https://leetcode.com/problems/single-number/

import pytest
from l00136_single_number import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        # --- LeetCode Official Examples ---
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        # --- Edge Cases & Constraints ---
        ([0, 0, 7], 7),  # Works with zeros
        ([-1, -1, -5], -5),  # Works with negative numbers
        ([10, -10, 5, 10, -10], 5),  # Mixed signs
        # --- Large Values ---
        ([10**9, 10**9, 500], 500),  # Large integer values
        ([2**31 - 1, 2**31 - 1, 2], 2),  # Boundary 32-bit values
    ],
)
def test_single_number_logic(sol, nums, expected):
    """
    Verifies that the XOR-based reduction correctly isolates the
    unique element in an array where all others appear twice.
    """
    result = sol.singleNumber(nums)
    assert result == expected, (
        f"Failed for nums={nums}: expected {expected}, got {result}"
    )


def test_single_number_integrity(sol):
    """
    Verify architectural integrity:
    Ensure the XOR operation handles a large volume of pairs efficiently O(N).
    """
    # 50,000 pairs of 1, and one unique 99
    large_input = [1, 1] * 50000 + [99]
    result = sol.singleNumber(large_input)
    assert result == 99
