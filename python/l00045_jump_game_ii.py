# 45 https://leetcode.com/problems/jump-game-ii/description/

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] + ([9999] * (n - 1))
        if n == 1:
            return 0
        if nums[0] == 0:
            return 9999  # Not possible to proceed
        for i in range(0, n - 1):
            for j in range(i + 1, min(n, i + nums[i] + 1)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n - 1]


class Solution2:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        current_jump_end = 0
        farthest = 0
        count = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                count += 1
                current_jump_end = farthest
                # farthest = 0   # This is not necessary, as farthest is same as current_jump_end right now
            if current_jump_end >= n - 1:
                return count
