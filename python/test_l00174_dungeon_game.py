# 174 - https://leetcode.com/problems/dungeon-game/

import pytest
from l00174_dungeon_game import Solution


@pytest.mark.parametrize(
    "dungeon, expected",
    [
        # LeetCode Case 1: Standard 3x3
        ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7),
        # LeetCode Case 2: Single zero
        ([[0]], 1),
        # Extra Case: Single cell negative
        ([[-10]], 11),
        # Extra Case: Single cell positive
        ([[10]], 1),
        # Extra Case: All healing
        ([[1, 2], [3, 4]], 1),
        # Corrected Damage Cases
        ([[-5, -10], [-2, -20]], 28),
        ([[-2, -100], [-1, -1]], 5),
        ([[-100, -100], [-100, -100]], 301),
        # Extra Case: Wide dungeon
        ([[-2, -3, -1]], 7),
        # Extra Case: Tall dungeon
        ([[-1], [-5], [10]], 7),
    ],
)
def test_calculate_minimum_hp(dungeon, expected):
    sol = Solution()
    result = sol.calculateMinimumHP(dungeon)

    grid_repr = f"{len(dungeon)}x{len(dungeon[0])} grid"
    assert result == expected, (
        f"Failed for {grid_repr}. Expected {expected}, got {result}. Input: {dungeon}"
    )


def test_empty_dungeon():
    """Validates the safety check for empty input returns 0."""
    sol = Solution()
    # Your code handles this gracefully with the 'if m == 0' check
    assert sol.calculateMinimumHP([]) == 0


def test_malformed_dungeon():
    """Validates the safety check for empty rows returns 0."""
    sol = Solution()
    # Your code handles this with the 'if n == 0' check
    assert sol.calculateMinimumHP([[]]) == 0
