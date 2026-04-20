# https://leetcode.com/problems/permutation-sequence/

# solve(nums, len, pos, k)
# {
#     if k == 0
#     {
#        return nums[:] // return a copy
#     }
#     knew = k
#     count = factorial(len-pos-1)
#     for (i = pos to len -1)
#     {
#         if (knew > count)
#         {
#             knew = knew - count
#         }
#         else
#         {
#             // swap
#             for (j=i to pos, descending)
#                 swap(j,j-1)

#             // recurse
#             return solve(nums, len, pos+1, list)

#             // undo swap
#             for (j=pos to i, ascending)
#                 swap(j,j+1)
#         }
#     }
#     return []
# }

# swap(nums,p1,p2)
#     temp = nums[p1]
#     nums[p1]=nums[p2]
#     nums[p2]=temp

# factorial(n)
#     if n==1 return 1
#     else return n*factorial(n-1)

# solve(nums, len(nums), 0, k)


class Solution:
    def __init__(self):
        # Cache factorials for N = 0 through 9
        self.fact = [1] * 10
        for i in range(2, 10):
            self.fact[i] = self.fact[i - 1] * i

    def swap(self, nums, p1, p2):
        nums[p1], nums[p2] = nums[p2], nums[p1]

    def solve_recursive(self, nums, length, pos, k):
        # Base case
        if pos == length:
            return "".join(map(str, nums))

        # Use the cached factorial
        count = self.fact[length - pos - 1]
        k_new = k

        for i in range(pos, length):
            if k_new > count:
                k_new -= count
            else:
                # Cyclic Shift: Move nums[i] to nums[pos]
                for j in range(i, pos, -1):
                    self.swap(nums, j, j - 1)

                # Recurse
                result = self.solve_recursive(nums, length, pos + 1, k_new)

                # Backtrack: Restore original order
                for j in range(pos, i):
                    self.swap(nums, j, j + 1)

                return result
        return ""

    def getPermutation(self, n: int, k: int) -> str:
        # Initial sorted list
        nums = list(range(1, n + 1))
        return self.solve_recursive(nums, n, 0, k)
