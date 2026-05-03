# 214 https://leetcode.com/problems/shortest-palindrome/

# 214 https://leetcode.com/problems/shortest-palindrome/

import pytest
from l00214_shortest_palindrome import Solution, Solution2, Solution3, Solution4


@pytest.mark.parametrize(
    "s, expected",
    [
        # --- LeetCode Original Case 1 ---
        ("aacecaaa", "aaacecaaa"),
        # --- LeetCode Original Case 2 ---
        ("abcd", "dcbabcd"),
        # --- Already a Palindrome ---
        ("aba", "aba"),
        ("racecar", "racecar"),
        ("aaaaa", "aaaaa"),
        # --- Single Character ---
        ("a", "a"),
        # --- Empty String ---
        ("", ""),
        # --- No Palindromic Prefix (except first char) ---
        ("abcd", "dcbabcd"),
        ("bcade", "edacbcade"),
        # --- Overlapping Patterns (KMP Stress Test) ---
        ("abacabae", "eabacabae"),
        ("aaba", "abaaba"),
        ("baac", "caabaac"),
        # --- Longest Prefix is just Two Characters ---
        ("aaace", "ecaaace"),
        # --- Suffix logic test ---
        ("abb", "bbabb"),
    ],
)
@pytest.mark.parametrize("sol", [Solution(), Solution2(), Solution3(), Solution4()])
def test_shortest_palindrome(sol, s: str, expected: str):
    observed = sol.shortestPalindrome(s)
    assert observed == expected, (
        f"Failed for string '{s}'. Expected '{expected}', but got '{observed}'"
    )
