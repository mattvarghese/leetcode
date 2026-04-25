# https://leetcode.com/problems/word-break/

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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

        # Work backwards from end of string
        for i in range(n - 1, -1, -1):
            node = root
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.is_word and dp[j + 1]:
                    dp[i] = True
                    break

        return dp[0]
