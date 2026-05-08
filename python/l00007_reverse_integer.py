# 7 https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        sign = "-" if x < 0 else ""
        x = abs(x)
        s = str(x)
        n = len(s)
        if n == 0:
            return 0
        ri = list(reversed(s))
        if len(ri) == 0:
            return 0
        r = sign + "".join(ri)
        newX = int(r, 10)
        maxInt = (2**31) - 1
        if (newX < ((-1 * maxInt) - 1)) or (newX > maxInt):
            return 0
        return newX


class Solution2:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed boundaries
        MAX_INT = 2**31 - 1  # 2147483647
        MIN_INT = -(2**31)  # -2147483648

        res = 0
        # Use abs to simplify math, handle sign at the end
        remain = abs(x)

        while remain:
            # 1. Pop the last digit
            pop = remain % 10
            remain //= 10

            # 2. Push it onto the result
            res = (res * 10) + pop

        # 3. Apply sign
        res = res if x >= 0 else -res

        # 4. Range check
        if res < MIN_INT or res > MAX_INT:
            return 0

        return res
