# 198 https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: list[int]) -> int:
        return self.rob_internal(nums, 0, len(nums) - 1)

    def rob_internal(self, nums: list[int], start: int, end: int) -> int:
        current_max, previous_max = 0, 0
        for i in range(start, end + 1, 1):
            temp = current_max
            current_max = max(current_max, previous_max + nums[i])
            previous_max = temp
        return current_max
