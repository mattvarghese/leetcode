# 1306 https://leetcode.com/problems/jump-game-iii/description/

# Problem description:
#  You are given an array of numbers, and a starting index s.
#  From any index, you may jump left of right exactly the value at that index.
#  Return the sequence of jumps - indices as a list - to find a value of 0.
#  If zero is not present or is unreachable, return an empty list
# Hint:
# It is possible there are cycles

from typing import List, Set


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        result = self.jump_to_zero(arr, start)
        return len(result) > 0

    def jump_to_zero(self, nums: List[int], k: int) -> List[int]:
        visited: Set[int] = set()
        result: List[int] = []
        self.jump_implementation(nums, k, visited, result)
        return result

    def jump_implementation(
        self, nums: List[int], current: int, visited: Set[int], result: List[int]
    ) -> bool:
        if current in visited:
            return False

        visited.add(current)
        result.append(current)

        curVal = nums[current]

        if curVal == 0:
            return True

        if (current - curVal) >= 0:
            if self.jump_implementation(nums, current - curVal, visited, result):
                return True

        if (current + curVal) < len(nums):
            if self.jump_implementation(nums, current + curVal, visited, result):
                return True

        result.pop()  # Remove this from the path
        # However, current can still stay in visited, because
        # regardless of how we get to current, there is no path from current to 0
        return False
