# https://leetcode.com/problems/word-break-ii/

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Build the Trie
        root = TrieNode()
        for word in wordDict:
            node = root
            for char in word:
                # Create branch if not already present
                if char not in node.children:
                    node.children[char] = TrieNode()
                # Move to branch
                node = node.children[char]
            # Mark node as word (but still may proceed)
            node.is_word = True

        # initializations
        n = len(s)
        # dp[i] holds "whether the substring s[i:] can be broken into words."
        dp = [False] * (n + 1)
        dp[n] = True  # Base case: empty string can be broken into words.

        dpw = [[False for _ in range(n)] for _ in range(n)]

        # Work backwards from end of string
        for i in range(n - 1, -1, -1):
            node = root
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.is_word and dp[j + 1]:
                    dp[i] = True
                    dpw[i][j] = True

        sentences: List[str] = []
        if not dp[0]:
            return sentences

        results: List[str] = []
        self.makeSentences(s, dp, dpw, 0, n, "", results)
        return results

    def makeSentences(
        self,
        s: str,
        dp: List[bool],
        dpw: List[List[bool]],
        start: int,
        n: int,
        current: str,
        results: List[str],
    ):
        if start >= n:
            results.append(current)
            return
        newWord = ""

        for i in range(start, n):
            if dpw[start][i] and dp[i + 1]:
                if current != "":
                    newWord = current + " " + s[start : i + 1]
                else:
                    newWord = s[start : i + 1]
                self.makeSentences(s, dp, dpw, i + 1, n, newWord, results)
