import os
import sys

import pytest

# Add the current directory to sys.path so importlib can find the file
sys.path.append(os.path.dirname(__file__))

from l00001_two_sum import solve


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([3, 3], 6, (0, 1)),
    ],
)
def test_solve(nums, target, expected):
    result = solve(nums, target)
    # Sorting both ensures the test passes even if indices are reversed
    assert tuple(sorted(result)) == tuple(sorted(expected))
