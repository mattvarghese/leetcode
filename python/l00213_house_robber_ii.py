# 213 https://leetcode.com/problems/house-robber-ii/


# Use previous solution
from typing import List

from l00198_house_robber import Solution as Solution1


class Solution(Solution1):
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob_internal(nums, 0, n - 2), self.rob_internal(nums, 1, n - 1))
