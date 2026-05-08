# 4 https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, n1
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = ((n1 + n2 + 1) // 2) - partition1
            left1 = float("-inf") if (partition1) <= 0 else nums1[partition1 - 1]
            right1 = float("inf") if (partition1) >= n1 else nums1[partition1]
            left2 = float("-inf") if (partition2) <= 0 else nums2[partition2 - 1]
            right2 = float("inf") if (partition2) >= n2 else nums2[partition2]

            if (left1 <= right2) and (left2 <= right1):
                if (n1 + n2) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return max(left1, left2)
            elif left1 > right2:
                high = partition1 - 1
            else:
                low = partition1 + 1
        raise ValueError("Input arrays are not sorted.")
