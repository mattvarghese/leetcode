# https://leetcode.com/problems/single-number-ii/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for n in nums:
            # 'ones' holds bits that appeared 1 time (but not 3)
            # 'twos' holds bits that appeared 2 times (but not 3)

            # Logic: Add bit to 'ones' if it's not already in 'twos'
            #   Take the current ones and XOR it with the new number n. Then, perform a BITAND with the BITNOT of twos.
            ones = (ones ^ n) & ~twos

            # Logic: Add bit to 'twos' if it's not already in 'ones'
            #   Take the current twos and XOR it with the new number n. Then, perform a BITAND with the BITNOT of the newly updated ones.
            twos = (twos ^ n) & ~ones

        return ones
