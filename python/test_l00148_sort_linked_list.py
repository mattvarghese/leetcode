# https://leetcode.com/problems/sort-list/

from typing import List, Optional

import pytest
from l00148_sort_linked_list import ListNode, Solution


def list_to_link(nums: List[int]) -> Optional[ListNode]:
    """Helper to convert Python list to Linked List."""
    if not nums:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in nums:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def link_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper to convert Linked List back to Python list for validation."""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


@pytest.mark.parametrize(
    "l",
    [
        # LeetCode Case 1
        ([4, 2, 1, 3]),
        # LeetCode Case 2
        ([-1, 5, 3, 4, 0]),
        # LeetCode Case 3: Empty List
        ([]),
        # Extra Case: Already Sorted
        ([1, 2, 3, 4, 5]),
        # Extra Case: Reversed (Worst case for some sorts)
        ([5, 4, 3, 2, 1]),
        # Extra Case: Identical values
        ([2, 2, 2, 2]),
        # Extra Case: Single element
        ([42]),
        # Extra Case: Large list (1000 elements)
        (list(range(1000, 0, -1))),
    ],
)
def test_sort_linked_list(l):
    # 1. Setup: Convert input to Linked List
    head = list_to_link(l)

    # 2. Execute: Perform sort
    s = Solution()
    sorted_head = s.sortList(head)

    # 3. Harvest: Convert back to list for easy validation
    result_list = link_to_list(sorted_head)

    # 4. Assert: Validate both order and integrity
    # We compare against Python's built-in sorted() to ensure all elements are present
    expected = sorted(l)

    # Using a professional f-string representation for failures
    list_repr = ", ".join(map(str, l))
    assert result_list == expected, (
        f"List <{list_repr}> was not sorted correctly. Got {result_list}"
    )
