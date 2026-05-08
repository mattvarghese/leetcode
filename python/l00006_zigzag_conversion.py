# 6 https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        n = len(s)
        skip = 2 * (numRows - 1)
        for j in range(0, numRows):
            for i in range(0, n, skip):
                if (i + j) < n:
                    result += s[i + j]
                if (j != 0) and ((j != (numRows - 1)) and ((i + skip - j) < n)):
                    result += s[i + skip - j]
        return result


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = []
        n = len(s)
        cycle_len = 2 * (numRows - 1)

        for r in range(numRows):
            for i in range(0, n - r, cycle_len):
                # 1. Add the vertical character
                res.append(s[i + r])

                # 2. Add the diagonal character (only if not top or bottom row)
                # The diagonal index is always: next_cycle_start - current_row
                diagonal_idx = i + cycle_len - r
                if 0 < r < numRows - 1 and diagonal_idx < n:
                    res.append(s[diagonal_idx])

        return "".join(res)
