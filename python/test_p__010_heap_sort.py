from typing import List

import pytest
from p__010_heap_sort import HeapSort


@pytest.mark.parametrize(
    "nums, expected",
    [
        # --- Standard Cases ---
        ([3, 2, 1, 5, 6, 4], [1, 2, 3, 4, 5, 6]),
        ([10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]),
        # --- Already Sorted & Reverse Sorted ---
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        # --- Duplicates ---
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
        # --- Negative Numbers ---
        ([-1, -5, 2, 10, -20], [-20, -5, -1, 2, 10]),
        ([0, -1, 1, -2, 2], [-2, -1, 0, 1, 2]),
        # --- Edge Cases ---
        ([], []),
        ([42], [42]),
        ([2, 1], [1, 2]),
        # --- Floating Point ---
        ([3.5, 2.1, 3.5, 1.0], [1.0, 2.1, 3.5, 3.5]),
    ],
)
def test_heap_sort_method(nums: List[int], expected: List[int]):
    """Tests the .sort() method for ascending order using Max-Heap."""
    # Use a copy to avoid mutating the input param if used elsewhere
    hs = HeapSort(list(nums), mode="max")
    observed = hs.sort()
    assert observed == expected, (
        f"HeapSort.sort() failed for {nums}. Expected {expected}, got {observed}"
    )


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 2, 1, 5, 6, 4], [1, 2, 3, 4, 5, 6]),
        ([10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]),
        ([-1, -5, 2, 10, -20], [-20, -5, -1, 2, 10]),
        ([2, 1], [1, 2]),
        ([], []),
    ],
)
def test_heap_sort_iterator_sorted(nums: List[int], expected: List[int]):
    """
    Tests that the iterator itself yields the sorted result.
    """
    hs = HeapSort(list(nums), mode="max")

    # This calls the __iter__ method
    observed = [item for item in hs]

    assert observed == expected, (
        f"Iterator failed for {nums}. Expected {expected}, got {observed}"
    )


def test_heap_sort_min_mode():
    """Verify that Min-Heap mode results in a descending sort."""
    nums = [3, 2, 1, 5, 6, 4]
    expected = [6, 5, 4, 3, 2, 1]
    hs = HeapSort(nums, mode="min")
    assert hs.sort() == expected, "Min-Heap sort should produce descending order."
