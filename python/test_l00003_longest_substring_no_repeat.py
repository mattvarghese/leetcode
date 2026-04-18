import os
import sys

import pytest

# Add the current directory to sys.path so the module can be discovered
sys.path.append(os.path.dirname(__file__))

from l00003_longest_substring_no_repeat import solve


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),  # Example 1: "abc"
        ("bbbbb", 1),  # Example 2: "b"
        ("pwwkew", 3),  # Example 3: "wke"
        ("", 0),  # Edge Case: Empty string
        (" ", 1),  # Edge Case: Single space
        ("au", 2),  # Short string
        ("dvdf", 3),  # Overlapping potential substrings
    ],
)
def test_solve(s, expected):
    """
    Validates the sliding window logic for finding the length of the
    longest substring without repeating characters.
    """
    result = solve(s)
    assert result == expected
