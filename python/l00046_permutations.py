# https://leetcode.com/problems/permutations/

from typing import List


def fun(nums, length, pos, result_list):
    # Base case: if we are at the last element, the permutation is complete
    if pos == length - 1:
        # Crucial: append a COPY of nums, otherwise all entries
        # in result_list will point to the same final array state.
        result_list.append(nums[:])
        return

    for i in range(pos, length):
        # 1. Capture left and right (same as your pseudocode)
        left = nums[pos]
        right = nums[i]

        # 2. Swap
        nums[pos] = right
        nums[i] = left

        # 3. Recurse to the next position
        fun(nums, length, pos + 1, result_list)

        # 4. Undo swap (Backtrack)
        nums[pos] = left
        nums[i] = right


def solve(nums: List[int]) -> List[List[int]]:
    result_list: List[List[int]] = []
    fun(nums, len(nums), 0, result_list)
    return result_list
