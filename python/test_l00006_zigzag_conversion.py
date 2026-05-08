import pytest
from l00006_zigzag_conversion import Solution, Solution2


@pytest.mark.parametrize(
    "s, numRows, expected",
    [
        # --- LeetCode Example 1 ---
        # P   A   H   N
        # A P L S I I G
        # Y   I   R
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        # --- LeetCode Example 2 ---
        # P     I    N
        # A   L S  I G
        # Y A   H R
        # P     I
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        # --- LeetCode Example 3 ---
        ("A", 1, "A"),
        # --- Boundary: Single Row ---
        # Should return the string as is
        ("ABCDE", 1, "ABCDE"),
        # --- Boundary: numRows >= String Length ---
        # Should return the string as is (vertical line)
        ("ABC", 5, "ABC"),
        # --- Boundary: Two Rows ---
        # Alternating characters: A C E / B D
        ("ABCDE", 2, "ACEBD"),
        # --- Longer String ---
        # G   S   G   S
        # E K F R E K
        # E   O   E
        ("GEEKSFORGEEKS", 3, "GSGSEKFREKEOE"),
        # --- Empty String ---
        ("", 3, ""),
    ],
)
@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_convert(sol, s, numRows, expected):
    assert sol.convert(s, numRows) == expected


@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_long_performance(sol):
    """Ensures the O(n) math-based approach handles long strings quickly."""
    s = "A" * 10000
    # Zigzagging a string of all the same characters should just return the same string
    assert sol.convert(s, 50) == s
