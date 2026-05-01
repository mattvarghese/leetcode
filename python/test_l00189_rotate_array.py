# 189 https://leetcode.com/problems/rotate-array/

import pytest
from l00189_rotate_array import Solution, Solution2


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # LeetCode Case 1
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        # LeetCode Case 2
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        # Edge Case: k is 0 (No rotation)
        ([1, 2, 3], 0, [1, 2, 3]),
        # Edge Case: k is equal to length (Full rotation)
        ([1, 2, 3], 3, [1, 2, 3]),
        # Edge Case: k is larger than length (Modular rotation)
        ([1, 2], 3, [2, 1]),
        # Edge Case: Single element
        ([1], 10, [1]),
        # Edge Case: Large rotation
        ([1, 2, 3, 4, 5], 11, [5, 1, 2, 3, 4]),
    ],
)
@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_rotate_array(nums, sol, k, expected):

    # We must pass a copy or a fresh list because it's in-place
    test_input = list(nums)
    sol.rotate(test_input, k)

    assert test_input == expected, (
        f"Failed for nums={nums}, k={k}. Expected {expected}, but got {test_input}"
    )
