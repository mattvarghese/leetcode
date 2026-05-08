# 15 https://leetcode.com/problems/3sum/


from collections import deque
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.mergeSort(nums, 0, n - 1)
        results: List[List[int]] = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            part = self.twoSum(-nums[i], nums, i + 1, n - 1)
            for oneRes in part:
                results.append([nums[i]] + oneRes)
        return results

    def twoSum(
        self, target: int, nums: List[int], start: int, end: int
    ) -> List[List[int]]:
        left, right = start, end
        results: List[List[int]] = []
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                results.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while right > left and nums[right] == nums[right + 1]:
                    right -= 1
            elif total > target:
                right -= 1
            else:
                left += 1
        return results

    def mergeSort(self, nums: List[int], start: int, end: int):
        if start >= end:
            return
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid + 1, end)
        i, j = start, mid + 1
        st = deque()
        # We only need to loop until the 'writer' i reaches the end
        while i <= end:
            # 1. If i is still in the first half, we MUST save the
            # original value before i overwrites it.
            if i <= mid:
                st.append(nums[i])

            # 2. Source from the stack (left side) and j (right side)
            leftVal = st[0] if st else float("inf")
            rightVal = nums[j] if j <= end else float("inf")

            # 3. Compare and write to nums[i]
            if leftVal <= rightVal:
                nums[i] = st.popleft()
            else:
                nums[i] = rightVal
                j += 1

            # 4. Move the writer forward
            i += 1
