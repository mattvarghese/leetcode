# 10 https://leetcode.com/problems/regular-expression-matching/

import pytest
from l00010_regular_expression_matching import Solution, Solution2


@pytest.mark.parametrize(
    "s, p, expected",
    [
        # --- LeetCode Example 1 ---
        ("aa", "a", False),
        # --- LeetCode Example 2 ---
        # "a*" matches "aa"
        ("aa", "a*", True),
        # --- LeetCode Example 3 ---
        # ".*" matches "ab"
        ("ab", ".*", True),
        # --- Dot matching ---
        ("abc", "a.c", True),
        ("abc", "a.d", False),
        # --- Multiple Stars ---
        # "a*b*" matches "aaabb"
        ("aaabb", "a*b*", True),
        # Empty string matches "a*b*"
        ("", "a*b*", True),
        # --- Complex Combinations ---
        ("mississippi", "mis*is*p*.", False),
        ("aab", "c*a*b", True),  # c* acts as zero occurrences
        ("aaa", "a*a", True),
        ("aaa", "ab*a*c*a", True),
        # --- Boundary Cases ---
        ("", "", True),
        ("a", "", False),
        ("", ".", False),
        ("", ".*", True),
        # --- Long matching ---
        ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False),
    ],
)
@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_is_match(sol, s, p, expected):
    assert sol.isMatch(s, p) == expected
