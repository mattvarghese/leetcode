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


#### How the Direct Math Works (for $n=4, k=9$):

# * Available digits: `[1, 2, 3, 4]`
# * Convert $k$ to 0-based: `k = 8`
# * **First digit:** There are $(4-1)! = 6$ permutations starting with each digit.
# * `index = 8 // 6 = 1`. The digit at index 1 is `2`. (Remove `2` from list)
# * `k = 8 % 6 = 2`.


# * **Second digit:** There are $(3-1)! = 2$ permutations starting with each remaining digit.
# * Remaining digits: `[1, 3, 4]`
# * `index = 2 // 2 = 1`. The digit at index 1 is `3`. (Remove `3` from list)
# * `k = 2 % 2 = 0`.


# * **Third digit:** There are $(2-1)! = 1$ permutation per remaining digit.
# * Remaining digits: `[1, 4]`
# * `index = 0 // 1 = 0`. The digit at index 0 is `1`. (Remove `1` from list)
# * `k = 0 % 1 = 0`.


# * **Fourth digit:** Remaining digits: `[4]`. Drop it in.
# * **Result:** `"2314"`


class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        # Precompute factorials up to n
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i

        # Create the pool of available digits
        numbers = [str(i) for i in range(1, n + 1)]

        # Convert k to 0-based index
        k -= 1
        result = []

        # Determine the digits from left to right
        for i in range(n, 0, -1):
            # How many permutations exist for the remaining slots?
            permutations_per_digit = fact[i - 1]

            # Find the index of the digit we need
            idx = k // permutations_per_digit

            # Append it and remove it from our available pool
            result.append(numbers.pop(idx))

            # Update k for the next position
            k %= permutations_per_digit

        return "".join(result)
