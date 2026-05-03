# 212 https://leetcode.com/problems/word-search-ii/

from typing import List

import pytest
from l00212_word_search_ii import Solution, Solution2


@pytest.mark.parametrize(
    "board, words, expected",
    [
        # --- LeetCode Original Case 1 ---
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["oath", "eat"],
        ),
        # --- LeetCode Original Case 2 ---
        ([["a", "b"], ["c", "d"]], ["abcb"], []),
        # --- Your Failing Case (The "hklf" logic) ---
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain", "hklf", "hf"],
            ["oath", "eat", "hklf", "hf"],
        ),
        # --- Edge Case: Single Letter ---
        ([["a"]], ["a"], ["a"]),
        # --- Edge Case: Empty/No Match ---
        ([["a", "b"], ["c", "d"]], ["xyz"], []),
        # --- Overlapping Words ---
        (
            [["a", "b", "a"], ["y", "z", "t"], ["a", "b", "a"]],
            ["aba", "aba"],
            ["aba"],  # Should only return unique instances
        ),
        # --- Prefix Handling ---
        ([["a", "p", "p", "l", "e"]], ["app", "apple", "apply"], ["app", "apple"]),
        # --- Long Snake Path (Backtracking stress test) ---
        (
            [["a", "b", "c"], ["f", "e", "d"], ["g", "h", "i"]],
            ["abcdefghi", "cfi"],
            ["abcdefghi"],
        ),
        # --- Reusing same cell (Should fail) ---
        (
            [["a", "b"], ["a", "b"]],
            ["aba"],
            [],  # Cannot use the same 'a' twice for 'aba'
        ),
    ],
)
@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_word_search_ii(
    sol, board: List[List[str]], words: List[str], expected: List[str]
):
    observed = sol.findWords(board, words)

    # Sorting both because the order of results in Word Search II
    # doesn't matter, but set equality or sorted list equality does.
    assert sorted(observed) == sorted(expected), (
        f"Failed for words {words}. Expected {expected}, but got {observed}"
    )
