# https://leetcode.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        # Ensure word2 is the shorter string to minimize space to O(min(N, M))
        if n < m:
            return self.minDistance(word2, word1)

        # dp[j] represents the edit distance for word1[:i] and word2[:j]
        dp = list(range(m + 1))

        for i in range(1, n + 1):
            # prev tracks the value of dp[i-1][j-1] (the diagonal)
            prev = dp[0]
            dp[0] = i  # Base case: distance between word1[:i] and empty word2

            for j in range(1, m + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    # Characters match: no new operation needed
                    dp[j] = prev
                else:
                    # Characters mismatch: 1 + min(Replace, Insert, Delete)
                    # prev = dp[i-1][j-1] (Replace)
                    # dp[j] = dp[i-1][j] (Delete from word1)
                    # dp[j-1] = dp[i][j-1] (Insert into word1)
                    dp[j] = 1 + min(prev, dp[j], dp[j - 1])
                prev = temp

        return dp[m]
