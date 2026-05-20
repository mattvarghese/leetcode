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


class SolutionFiveAndTwo:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        fours = 0

        for n in nums:
            # 1. Update the 3-bit binary counter
            # 'fours' flips if there's a carry from 'twos' and 'ones'
            fours = fours ^ (twos & ones & n)
            # 'twos' flips if there's a carry from 'ones'
            twos = twos ^ (ones & n)
            # 'ones' toggles every single time the bit appears
            ones = ones ^ n

            # 2. Condition for state 5 (binary 101): fours == 1 and ones == 1
            # We create a mask of all bit positions that have hit exactly 5 encounters
            reset = fours & ones

            # 3. Force reset those specific bit positions back to 0
            ones = ones & ~reset
            twos = twos & ~reset
            fours = fours & ~reset

        # Target appears 2 times -> State 010 (fours=0, twos=1, ones=0)
        return twos


class SolutionOtherAndTarget:
    def singleNumber(self, nums: List[int], target: int, others: int) -> int:
        # 1. Determine how many state bits we need to track the 'others' count
        # (e.g., if others = 5 (101 in binary), we need 3 bits)
        num_bits = others.bit_length()

        # State array tracking the bit accumulators: state[0] is ones, state[1] is twos, etc.
        state = [0] * num_bits

        for n in nums:
            # 2. Simulate a full generic bitwise adder
            # To simulate carries correctly, we must update from the highest bit down to the lowest bit,
            # or track carries explicitly using a lookahead logic.
            carry = n
            for i in range(num_bits):
                next_carry = state[i] & carry
                state[i] ^= carry
                carry = next_carry

            # 3. Create the Reset Mask dynamically based on the binary definition of 'others'
            # Start with a mask of all 1s (effectively -1 or 0xFFFFFFFF in bitwise logic)
            reset_mask = ~0
            for i in range(num_bits):
                if (others >> i) & 1:
                    # If the i-th bit of 'others' is 1, include state[i] in our reset trigger
                    reset_mask &= state[i]

            # 4. Apply the reset mask to clear counters that hit the 'others' threshold
            for i in range(num_bits):
                state[i] &= ~reset_mask

        # 5. Extract the answer using the binary definition of 'target'
        # Find the first active bit position in the target configuration to read out the answer
        for i in range(num_bits):
            if (target >> i) & 1:
                return state[i]

        return 0
