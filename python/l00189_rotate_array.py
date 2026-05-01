# 189 https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k % n
        temp = nums[n - k :]
        for j in range(n - 1, k - 1, -1):
            nums[j] = nums[j - k]
        for i in range(k):
            nums[i] = temp[i]


class Solution2:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0:
            return

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # The "Triple Reverse" trick
        reverse(0, n - 1)  # Reverse entire array
        reverse(0, k - 1)  # Reverse first k elements
        reverse(k, n - 1)  # Reverse the remaining elements
