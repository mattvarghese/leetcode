# 215 https://leetcode.com/problems/kth-largest-element-in-an-array/

import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Note: targetIdx is k-1, as indices start with 0
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    def quickSelect(self, nums: List[int], low: int, high: int, targetIdx: int) -> int:
        p = random.randint(low, high)
        pVal = nums[p]
        nums[high], nums[p] = nums[p], nums[high]
        pointer = low
        for i in range(low, high):
            if nums[i] > pVal:  # sort descending
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1
        nums[pointer], nums[high] = nums[high], nums[pointer]
        if pointer < targetIdx:
            return self.quickSelect(nums, pointer + 1, high, targetIdx)
        elif pointer > targetIdx:
            return self.quickSelect(nums, low, pointer - 1, targetIdx)
        else:
            return nums[pointer]


class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Note: targetIdx is k-1, as indices start with 0
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    def quickSelect(self, nums: List[int], low: int, high: int, targetIdx: int) -> int:
        pivot = nums[random.randint(low, high)]
        lt, gt = low, high
        i = low
        while i <= gt:
            # We want to find the k-th largest, so we must sort descending on the
            # portions of the list we care to look at
            if nums[i] > pivot:  # Elements greater than pivot must move left
                nums[i], nums[lt] = nums[lt], nums[i]
                i = i + 1
                lt = lt + 1
            elif nums[i] < pivot:  # Elements less than pivot must move right
                nums[i], nums[gt] = nums[gt], nums[i]
                gt = gt - 1
            else:  # Skip over elements equal to pivot
                i = i + 1
        if targetIdx < lt:
            return self.quickSelect(nums, low, lt - 1, targetIdx)
        elif targetIdx > gt:
            return self.quickSelect(nums, gt + 1, high, targetIdx)
        else:
            return nums[lt]


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = k - 1
        low, high = 0, len(nums) - 1

        while low <= high:
            pivot = nums[random.randint(low, high)]

            # 3-way partition (Dutch National Flag algorithm)
            # lt: elements > pivot (since we want descending)
            # gt: elements < pivot
            # i: current element
            lt = low
            gt = high
            i = low

            while i <= gt:
                if nums[i] > pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                elif nums[i] < pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            # Now: nums[low...lt-1] > pivot
            #      nums[lt...gt] == pivot
            #      nums[gt+1...high] < pivot

            if target < lt:
                high = lt - 1
            elif target > gt:
                low = gt + 1
            else:
                # target is within the range of elements equal to pivot
                return nums[target]
