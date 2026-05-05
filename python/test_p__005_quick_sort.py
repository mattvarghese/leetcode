from typing import List

import pytest
from p__005_quick_sort import QuickSort, QuickSort2


@pytest.mark.parametrize(
    "nums, expected",
    [
        # --- Standard Cases ---
        ([3, 2, 1, 5, 6, 4], [1, 2, 3, 4, 5, 6]),
        ([10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]),
        # --- Already Sorted & Reverse Sorted ---
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        # --- Duplicates (The "Lomuto Stress Test") ---
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
        ([3, 3, 1, 2, 3, 2, 1], [1, 1, 2, 2, 3, 3, 3]),
        # --- Negative Numbers ---
        ([-1, -5, 2, 10, -20], [-20, -5, -1, 2, 10]),
        ([0, -1, 1, -2, 2], [-2, -1, 0, 1, 2]),
        # --- Edge Cases: Empty, Single, and Double ---
        ([], []),
        ([42], [42]),
        ([2, 1], [1, 2]),
        ([1, 2], [1, 2]),
        # --- Large Values & Large Range ---
        ([1000, 1, 500, -100, 0], [-100, 0, 1, 500, 1000]),
        # --- Floating Point (If your implementation supports them) ---
        ([3.5, 2.1, 3.5, 1.0], [1.0, 2.1, 3.5, 3.5]),
    ],
)
@pytest.mark.parametrize("qk", [QuickSort(), QuickSort2()])
def test_quicksort(qk, nums: List[int], expected: List[int]):
    observed = qk.Sort(nums)
    assert expected == observed, (
        f"Quicksort failed for {nums}, Expected={expected} but Observed={observed}."
    )
