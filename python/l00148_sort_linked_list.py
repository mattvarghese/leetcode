# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListEntry:
    def __init__(self, length: int, head: ListNode):
        self.length = length
        self.head = head


class Solution1:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head

        listsStack: List[ListEntry] = []
        current = head
        while (len(listsStack) > 1) or (current is not None):
            stackLen = len(listsStack)
            if (stackLen > 1) and (
                listsStack[stackLen - 1].length >= listsStack[stackLen - 2].length
            ):
                # Top two entries of stack are long enough to merge
                le1 = listsStack.pop()
                le2 = listsStack.pop()
                leNew = self.mergeListEntries(le1, le2)
                listsStack.append(leNew)
            elif current is not None:
                # There are more entries in source list
                leNew = ListEntry(1, current)
                previous = current
                current = current.next
                count = 1
                while (current is not None) and (previous.val <= current.val):
                    previous = current
                    count += 1
                    current = current.next
                previous.next = None
                leNew.length = count
                listsStack.append(leNew)
            else:
                # Ran out of list, so now just keep merging stack
                while len(listsStack) > 1:
                    le1 = listsStack.pop()
                    le2 = listsStack.pop()
                    leNew = self.mergeListEntries(le1, le2)
                    listsStack.append(leNew)
        # At this point, listStack will have exactly one entry
        result = listsStack.pop()
        return result.head

    def mergeListEntries(self, le1: ListEntry, le2: ListEntry) -> ListEntry:
        if le1.head is None:
            return le2
        elif le2.head is None:
            return le1

        head, previous, current = None, None, None
        le1head, le2head = le1.head, le2.head
        while (le1head is not None) and (le2head is not None):
            if le1head.val < le2head.val:
                current = le1head
                le1head = le1head.next
            else:
                current = le2head
                le2head = le2head.next
            if head is None:
                head = current
            else:
                previous.next = current
            previous = current

        if le1head is None:
            previous.next = le2head
        else:
            previous.next = le1head

        return ListEntry(le1.length + le2.length, head)


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1. Get the total length of the linked list: O(N)
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head

        # 2. Iteratively merge sub-lists of size 1, 2, 4, 8, etc.
        step = 1
        while step < length:
            prev = dummy
            curr = dummy.next

            while curr:
                # Extract the left sub-list of length 'step'
                left = curr
                right = self.split(left, step)

                # Extract the right sub-list of length 'step' and isolate the rest of the list
                curr = self.split(right, step)

                # Merge the two isolated sub-lists and link them back into the chain
                merged_head, merged_tail = self.merge(left, right)
                prev.next = merged_head
                prev = merged_tail

            step *= 2  # Double the chunk size for the next pass

        return dummy.next

    def split(self, head: ListNode, step: int) -> Optional[ListNode]:
        """Splits off a sub-list of the given step size from the head.

        Returns the head of the REMAINING list.
        """
        if not head:
            return None

        # Advance 'step - 1' times to find the end of the current block
        for _ in range(step - 1):
            if head.next:
                head = head.next
            else:
                break

        # Disconnect the block from the rest of the list
        remaining = head.next
        head.next = None
        return remaining

    def merge(self, l1: ListNode, l2: ListNode) -> tuple[ListNode, ListNode]:
        """Merges two sorted lists.

        Returns a tuple of (merged_head, merged_tail).
        """
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach any remaining trailing elements
        tail.next = l1 if l1 else l2

        # Fast-forward tail to the very end of the merged list segment
        while tail.next:
            tail = tail.next

        return dummy.next, tail
