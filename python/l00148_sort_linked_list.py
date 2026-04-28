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


class Solution:
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
