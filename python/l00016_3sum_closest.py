# 16 https://leetcode.com/problems/3sum-closest/description/

from collections import deque


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        self.mergeSort(nums, 0, n - 1)
        closest = self.twoSumClosest(target, nums[0], nums, 1, n - 1)
        i = 1
        while i < (n - 2):
            if nums[i] == nums[i - 1]:
                i = i + 1
                continue
            newClosest = self.twoSumClosest(target, nums[i], nums, i + 1, n - 1)
            if abs(target - newClosest) < abs(target - closest):
                closest = newClosest
            i += 1
        return closest

    def twoSumClosest(
        self, target: int, numI: int, nums: list[int], start: int, end: int
    ) -> int:
        left, right = start, end
        closest = numI + nums[start] + nums[end]
        while left < right:
            total = numI + nums[left] + nums[right]
            if abs(target - total) < abs(target - closest):
                closest = total
            if total <= target:
                left += 1
            if total >= target:
                right -= 1
        return closest

    def mergeSort(self, nums: list[int], start: int, end: int):
        if start >= end:
            return
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid + 1, end)

        left, right = start, mid + 1
        st = deque()
        while left <= end:
            if left <= mid:
                st.append(nums[left])
            leftVal = st[0] if len(st) > 0 else float("inf")
            rightVal = nums[right] if right <= end else float("inf")
            if leftVal <= rightVal:
                nums[left] = st.popleft()
            else:
                nums[left] = rightVal
                right += 1
            left += 1


class Solution2:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # Initialize with the first possible triplet sum
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # Minor optimization: skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                if curr_sum == target:
                    return curr_sum

                # Update closest if the current delta is smaller
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target:
                    l += 1
                else:
                    r -= 1

        return closest_sum
