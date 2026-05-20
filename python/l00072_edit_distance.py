# https://leetcode.com/problems/edit-distance/


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        # dp[i][j] represents the edit distance for word1[:i] and word2[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base Cases:
        # Transforming word1[:i] into an empty word2 requires i deletions
        for i in range(n + 1):
            dp[i][0] = i

        # Transforming an empty word1 into word2[:j] requires j insertions
        for j in range(m + 1):
            dp[0][j] = j

        # Fill the matrix row by row
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Match: Take the diagonal value directly
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Mismatch: 1 + min(Replace, Delete, Insert)
                    replace = dp[i - 1][j - 1]  # Diagonal top-left
                    delete = dp[i - 1][j]  # Directly above (same column, previous row)
                    insert = dp[i][j - 1]  # Directly left (same row, previous column)

                    dp[i][j] = 1 + min(replace, delete, insert)

        return dp[n][m]


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
