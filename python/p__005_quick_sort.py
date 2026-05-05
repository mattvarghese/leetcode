import random
from typing import List


class QuickSort:
    def Sort(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums: List[int], low: int, high: int):
        if low < 0 or high >= len(nums) or low >= high:
            return
        pointer = self.partition(nums, low, high)
        self.quickSort(nums, low, pointer - 1)
        self.quickSort(nums, pointer + 1, high)

    def partition(self, nums: List[int], low: int, high: int) -> int:
        p = random.randint(low, high)
        pVal = nums[p]
        nums[high], nums[p] = nums[p], nums[high]
        pointer = low
        for i in range(low, high):
            if nums[i] < pVal:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
        nums[pointer], nums[high] = nums[high], nums[pointer]
        return pointer


class QuickSort2:
    def Sort(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums: List[int], low: int, high: int):
        if low < 0 or high >= len(nums) or low >= high:
            return
        (lt, gt) = self.partition(nums, low, high)
        self.quickSort(nums, low, lt - 1)
        self.quickSort(nums, gt + 1, high)

    def partition(self, nums: List[int], low: int, high: int) -> (int, int):
        pivot = nums[random.randint(low, high)]
        lt = low
        gt = high
        i = low
        while i <= gt:
            if nums[i] < pivot:
                nums[i], nums[lt] = nums[lt], nums[i]
                i += 1
                lt += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        return (lt, gt)
