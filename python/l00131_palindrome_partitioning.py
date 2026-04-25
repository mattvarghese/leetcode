# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        lS = len(s)
        dp = [[False for _ in range(lS)] for _ in range(lS)]
        self.buildDp(s, lS, dp)
        results: List[List[str]] = []
        self.recursePart(s, lS, 0, dp, [], results)
        return results

    def buildDp(self, s: str, len: int, dp: List[List[bool]]):
        for i in range(len - 1, -1, -1):
            for j in range(i, len):
                if s[i] == s[j]:
                    # if odd single char, i=j
                    # if even double char, i=j+1
                    # else, check that s[i+1,j-1] is a palindrome
                    if j - i < 3 or dp[i + 1][j - 1]:
                        dp[i][j] = True

    def recursePart(
        self,
        s: str,
        lS: int,
        start: int,
        dp: List[List[bool]],
        current: List[str],
        results: List[List[str]],
    ):
        if start == lS:
            results.append(current[:])
        else:
            for endI in range(start, lS):
                if dp[start][endI]:
                    current.append(s[start : endI + 1])
                    self.recursePart(s, lS, endI + 1, dp, current, results)
                    current.pop()


# This is only better at large values of len(s)
class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]

        # 1. Preprocessing: Insert separators to handle even-length palindromes
        # "aba" -> "#a#b#a#"
        t = "#" + "#".join(s) + "#"
        n = len(t)
        radii = [0] * n
        center = right = 0

        # 2. Manacher's Algorithm to find all palindromic radii in O(N)
        for i in range(n):
            if i < right:
                mirror = 2 * center - i
                radii[i] = min(right - i, radii[mirror])

            # Attempt to expand around center i
            while (
                i + radii[i] + 1 < n
                and i - radii[i] - 1 >= 0
                and t[i + radii[i] + 1] == t[i - radii[i] - 1]
            ):
                radii[i] += 1

            # Update center and right boundary if expanded past current right
            if i + radii[i] > right:
                center = i
                right = i + radii[i]

        # 3. Backtracking using the radii for O(1) checks
        results = []
        self._backtrack(s, 0, radii, [], results)
        return results

    def _is_palindrome(self, start: int, end: int, radii: List[int]) -> bool:
        # Map original string indices (start, end) to the transformed string 't'
        # Original s[start:end+1] center in 't' is (start + end + 1)
        t_center = start + end + 1
        length = end - start + 1
        return radii[t_center] >= length

    def _backtrack(
        self,
        s: str,
        start: int,
        radii: List[int],
        current: List[str],
        results: List[List[str]],
    ):
        if start == len(s):
            results.append(list(current))
            return

        for end in range(start, len(s)):
            if self._is_palindrome(start, end, radii):
                current.append(s[start : end + 1])
                self._backtrack(s, end + 1, radii, current, results)
                current.pop()
