# https://leetcode.com/problems/max-points-on-a-line/

import pytest
from l00149_max_points import Solution


@pytest.mark.parametrize(
    "points, expected",
    [
        # LeetCode Case 1: Simple diagonal
        ([[1, 1], [2, 2], [3, 3]], 3),
        # LeetCode Case 2: Mixed slopes
        ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
        # Vertical Line Case
        ([[1, 1], [1, 2], [1, 10], [2, 2]], 3),
        # Horizontal Line Case
        ([[1, 1], [2, 1], [10, 1], [2, 2]], 3),
        # Duplicate Points (Problem statement says points are unique, but good to handle)
        ([[1, 1], [1, 1], [2, 2]], 3),
        # Single Point
        ([[1, 1]], 1),
        # Two Points (Always 2)
        ([[1, 1], [5, 5]], 2),
        # Large Square (No more than 2 on any line)
        ([[0, 0], [0, 1], [1, 0], [1, 1]], 2),
        # Precision Test: Slopes that are very close but not equal
        # (1/2 vs 2/4 is same, but 100/201 vs 50/101 is NOT)
        ([[0, 0], [201, 100], [101, 50]], 2),
        # Stress Test: 300 points on 3 different lines
        (
            [[i, i] for i in range(100)]
            + [[i, 2 * i] for i in range(100)]
            + [[i, 0] for i in range(100)],
            102,  # Note - (0,0) appears thrice
        ),
    ],
)
def test_max_points(points, expected):
    sol = Solution()
    result = sol.maxPoints(points)

    # Custom error message using the formatting we discussed
    points_repr = str(points) if len(points) < 10 else f"{len(points)} points"
    assert result == expected, (
        f"Failed for {points_repr}. Expected {expected}, got {result}"
    )


def test_empty_input():
    sol = Solution()
    assert sol.maxPoints([]) == 0
