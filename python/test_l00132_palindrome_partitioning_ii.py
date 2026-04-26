# https://leetcode.com/problems/palindrome-partitioning-ii/

import pytest
from l00132_palindrome_partitioning_ii import Solution, Solution2


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aab", 1),  # "aa" | "b"
        ("a", 0),  # No cuts needed
        ("ab", 1),  # "a" | "b"
        ("aba", 0),  # Already a palindrome
        ("abcccba", 0),  # Already a palindrome
        ("racecar", 0),  # Already a palindrome
        ("abcde", 4),  # All unique, must cut every char
        ("aaaaa", 0),  # All same, no cuts
        ("apapples", 4),  # "apa" | "pp" | "l" | "e" | "s"
    ],
)
@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_min_cut(sol, s, expected):
    assert sol.minCut(s) == expected
