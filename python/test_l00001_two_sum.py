import os
import sys

import pytest

# Add the current directory to sys.path so importlib can find the file
sys.path.append(os.path.dirname(__file__))

from l00001_two_sum import solve, solve2


@pytest.mark.parametrize("func", [solve, solve2])
@pytest.mark.parametrize(
    "nums, target",
    [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 5, 5, 9], 10),  # This will now pass for both (1, 2) and (0, 3)
    ],
)
def test_two_sum_implementations(func, nums, target):
    result = func(nums, target)

    # 1. Verify that a result was actually returned
    assert len(result) == 2, f"{func.__name__} failed to find a solution"

    # 2. Extract indices
    idx1, idx2 = result

    # 3. Ensure the indices are unique (cannot use the same element twice)
    assert idx1 != idx2, f"{func.__name__} returned the same index twice"

    # 4. Ensure indices are within the valid range of the list
    assert 0 <= idx1 < len(nums)
    assert 0 <= idx2 < len(nums)

    # 5. The core check: Do the values at these indices add up to the target?
    actual_sum = nums[idx1] + nums[idx2]
    assert actual_sum == target, (
        f"{func.__name__} returned indices {idx1}, {idx2} "
        f"({nums[idx1]} + {nums[idx2]}), which sums to {actual_sum} instead of {target}"
    )
