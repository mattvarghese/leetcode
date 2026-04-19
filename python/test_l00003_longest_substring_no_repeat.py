import os
import sys

import pytest

# Add the current directory to sys.path
sys.path.append(os.path.dirname(__file__))

# Import both implementations
from l00003_longest_substring_no_repeat import solve, solve2


@pytest.mark.parametrize("func", [solve, solve2])
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
        ("abba", 2),  # Crucial Case: Ensures left pointer doesn't move backward
        ("tmmzuxt", 5),  # Long complex case
    ],
)
def test_longest_substring(func, s, expected):
    """
    Validates that both sliding window implementations correctly calculate
    the length of the longest substring without repeating characters.
    """
    result = func(s)
    assert result == expected, (
        f"Failed for '{s}' using {func.__name__}. Expected {expected}, got {result}"
    )
