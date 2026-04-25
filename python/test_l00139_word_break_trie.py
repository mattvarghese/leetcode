# https://leetcode.com/problems/word-break/

import pytest
from l00139_word_break_trie import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "s, wordDict, expected",
    [
        # --- LeetCode Official Examples ---
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        # --- Edge Cases & Constraints ---
        ("a", ["a"], True),  # Single character match
        ("a", ["b"], False),  # Single character mismatch
        ("", ["a"], True),  # Empty string (base case)
        ("abcd", [], False),  # Empty dictionary
        ("abc", ["abcd"], False),  # Word longer than string
        # --- Pattern Overlaps ---
        ("aaaa", ["aa"], True),  # Multiple use of same word
        ("aaaaaaa", ["aaaa", "aaa"], True),  # Overlapping possible starts
        # --- Performance / TLE Protection ---
        # The "Deep Abyss" case: many prefixes, but fails at the very end
        ("a" * 50 + "b", ["a", "aa", "aaa", "aaaa", "aaaaa"], False),
    ],
)
def test_word_break_logic(sol, s, wordDict, expected):
    """
    Verifies that the wordBreak function correctly identifies
    if the string can be segmented into dictionary words.
    """
    result = sol.wordBreak(s, wordDict)
    assert result == expected, (
        f"Failed for s='{s[:20]}...', wordDict={wordDict}: "
        f"expected {expected}, got {result}"
    )


def test_word_break_integrity(sol):
    """
    Verify architectural integrity:
    Large inputs should not trigger RecursionError if DP is implemented.
    """
    # A string long enough to hit default recursion limits (1000)
    # but short enough for an O(N^2) DP to solve instantly.
    s = "a" * 1500
    wordDict = ["a"]

    try:
        result = sol.wordBreak(s, wordDict)
        assert result is True
    except RecursionError:
        pytest.fail(
            "Solution triggered a RecursionError! Use Iterative DP or Memoization."
        )
