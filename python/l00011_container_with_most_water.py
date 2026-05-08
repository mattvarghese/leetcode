# 11 https://leetcode.com/problems/container-with-most-water/description/


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxA = 0
        while left < right:
            maxA = max(maxA, ((right - left) * min(height[left], height[right])))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxA
