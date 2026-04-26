# https://leetcode.com/problems/edit-distance/

import pytest
from l00072_edit_distance import Solution


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("horse", "ros", 3),  # h->r, r dropped, e dropped
        ("intention", "execution", 5),
        ("", "", 0),  # Empty identity
        ("a", "", 1),  # Single deletion
        ("", "a", 1),  # Single insertion
        ("abc", "abc", 0),  # Already identical
        ("abc", "def", 3),  # Complete replacement
        ("plasma", "altruism", 6),  # Complex shift
    ],
)
def test_edit_distance(word1, word2, expected):
    sol = Solution()
    assert sol.minDistance(word1, word2) == expected
