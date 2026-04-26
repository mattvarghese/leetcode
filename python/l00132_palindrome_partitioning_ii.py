# https://leetcode.com/problems/palindrome-partitioning-ii/

from typing import List, Tuple


class Solution2:
    def minCut(self, s: str) -> int:
        if s == "":
            return 0
        lS = len(s)
        dp = [[False for _ in range(lS)] for _ in range(lS)]
        self.buildDp(s, lS, dp)
        if dp[0][lS - 1]:
            return 0
        dp2: List[int] = [lS for _ in range(lS)]
        for endS in range(0, lS):
            minCuts = endS
            if dp[0][endS]:
                minCuts = 0
            else:
                for i in range(endS, -1, -1):
                    if dp[i][endS]:
                        minCuts = min(minCuts, 1 + dp2[i - 1])
                    if minCuts == 1:
                        break
            dp2[endS] = minCuts
        return dp2[lS - 1]

    def buildDp(self, s: str, len: int, dp: List[List[bool]]):
        for i in range(len - 1, -1, -1):
            for j in range(i, len):
                if s[i] == s[j]:
                    # if odd single char, i=j
                    # if even double char, i=j+1
                    # else, check that s[i+1,j-1] is a palindrome
                    if j - i < 3 or dp[i + 1][j - 1]:
                        dp[i][j] = True


class Solution:
    def minCut(self, s: str) -> int:
        if s == "":
            return 0
        lS = len(s)
        dp = [[-1, -1] for _ in range(lS)]

        for center in range(lS):
            # Odd length palindromes (like "aba")
            self.expand(s, center, center, dp)
            # Even length palindromes (like "aa")
            self.expand(s, center, center + 1, dp)

        if self.isPalindrome(dp, 0, lS - 1):
            return 0
        dp2: List[int] = [lS for _ in range(lS)]
        for endS in range(0, lS):
            minCuts = endS
            if self.isPalindrome(dp, 0, endS):
                minCuts = 0
            else:
                for i in range(endS, -1, -1):
                    if self.isPalindrome(dp, i, endS):
                        minCuts = min(minCuts, 1 + dp2[i - 1])
                        if minCuts == 1:
                            break
            dp2[endS] = minCuts
        return dp2[lS - 1]

    def isPalindrome(self, dp: List[Tuple[int, int]], start: int, end: int):
        isEven = ((end - start + 1) % 2) == 0
        mid: int = start + ((end - start) // 2)
        lenP = 1 + ((end - start) // 2)
        if (isEven and dp[mid][1] >= lenP) or ((not isEven) and dp[mid][0] >= lenP):
            return True
        return False

    def expand(self, s: str, CLeft: int, CRight: int, dp):
        left = CLeft
        right = CRight
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # If palindrome still
            if CLeft == CRight:
                dp[CLeft][0] = max(dp[CLeft][0], CLeft - left + 1)
            else:
                dp[CLeft][1] = max(dp[CLeft][1], CLeft - left + 1)
            left -= 1
            right += 1
