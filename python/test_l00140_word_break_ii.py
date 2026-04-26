# https://leetcode.com/problems/word-break-ii/

import pytest
from l00140_word_break_ii import Solution


@pytest.mark.parametrize(
    "s, wordDict, expected",
    [
        (
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"],
            ["cat sand dog", "cats and dog"],
        ),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"],
        ),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
        ("aaaaaaa", ["aaaa", "aaa"], ["aaaa aaa", "aaa aaaa"]),
    ],
)
def test_word_break_ii(s, wordDict, expected):
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    # Sort both to ensure comparison works regardless of order
    assert sorted(result) == sorted(expected)
