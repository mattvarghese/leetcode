# https://leetcode.com/problems/palindrome-partitioning/

import pytest
from l00131_palindrome_partitioning import Solution, Solution2


@pytest.mark.parametrize("sol", [Solution(), Solution2()])
@pytest.mark.parametrize(
    "s, expected",
    [
        # --- LeetCode Official Examples ---
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        # --- Edge Cases & Constraints ---
        ("", [[]]),  # Empty string case
        ("aba", [["a", "b", "a"], ["aba"]]),  # String itself is a palindrome
        ("abcdef", [["a", "b", "c", "d", "e", "f"]]),  # No palindromes longer than 1
        # --- Repeated Characters ---
        (
            "aaaa",
            [
                ["a", "a", "a", "a"],
                ["a", "a", "aa"],
                ["a", "aa", "a"],
                ["aa", "a", "a"],
                ["aa", "aa"],
                ["a", "aaa"],
                ["aaa", "a"],
                ["aaaa"],
            ],
        ),
    ],
)
def test_partition_logic(sol, s, expected):
    """
    Verifies that the partitioning logic finds all possible ways to
    split the string into palindromic substrings.
    """
    result = sol.partition(s)

    # Sort both results for deterministic comparison regardless of backtracking order
    actual_sorted = sorted([sorted(p) for p in result])
    expected_sorted = sorted([sorted(e) for e in expected])

    assert actual_sorted == expected_sorted, (
        f"Failed for s='{s}': expected {len(expected)} partitions, got {len(result)}"
    )


@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_partition_integrity(sol):
    """
    Verify architectural integrity:
    Every substring in every partition must be a palindrome.
    """
    s = "aabbc"
    result = sol.partition(s)

    for partition in result:
        # 1. Join must recreate the original string
        assert "".join(partition) == s

        # 2. Each part must be a palindrome
        for part in partition:
            assert part == part[::-1], f"Found non-palindrome substring: {part}"


@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_performance_limit(sol):
    """
    Verify that the system handles larger inputs without hitting
    recursion limits or excessive TLE (up to a reasonable N=16).
    """
    s = "a" * 16
    result = sol.partition(s)
    # The number of partitions for 'a'*n is 2^(n-1)
    assert len(result) == 2 ** (16 - 1)
