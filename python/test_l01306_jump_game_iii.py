import pytest
from l01306_jump_game_iii import Solution


@pytest.mark.parametrize(
    "arr, start, expected_path_exists",
    [
        # --- LeetCode Example 1 ---
        # Path: 5 -> 1 -> 4 -> 2 -> 0 (indices: 5, 4, 2)
        ([4, 2, 3, 0, 3, 1, 2], 5, True),
        # --- LeetCode Example 2 ---
        # Path: 0 -> 2 -> 3 (index 3 is value 0)
        ([4, 2, 3, 0, 3, 1, 2], 0, True),
        # --- LeetCode Example 3 ---
        # No way to reach index 1 (value 0)
        ([3, 0, 2, 1, 2], 2, False),
        # --- Simple Success ---
        ([1, 0], 0, True),
        ([0], 0, True),
        # --- Cycle: Infinite Loop (No Zero) ---
        # 0 -> 2 -> 0 ...
        ([2, 5, 2], 0, False),
        # --- Cycle: With Reachable Zero ---
        # 0 -> 2 -> 0 is a cycle, but 0 -> 2 -> 4 is index of 0
        ([2, 1, 2, 1, 0], 0, True),
        # --- Dead End (Bounds) ---
        # 10 is way out of bounds
        ([10, 5, 2, 0], 0, False),
        # --- Multiple Zeros ---
        ([2, 0, 2, 0], 0, False),
        # --- Large Gap Success ---
        # 0 -> 4 -> 3 -> 2 -> 1 -> 0
        ([4, 1, 1, 1, 0], 0, True),
        # --- Value is larger than array length ---
        ([100, 100, 0], 0, False),
    ],
)
def test_can_reach(arr, start, expected_path_exists):
    sol = Solution()
    # The LeetCode method signature returns bool
    assert sol.canReach(arr, start) == expected_path_exists


@pytest.mark.parametrize(
    "arr, start, expected_val",
    [
        # Validate that the path actually leads to a 0
        ([4, 2, 3, 0, 3, 1, 2], 5, 0),
        ([4, 2, 3, 0, 3, 1, 2], 0, 0),
        ([1, 1, 1, 0], 0, 0),
    ],
)
def test_path_validity(arr, start, expected_val):
    sol = Solution()
    path = sol.jump_to_zero(arr, start)

    assert len(path) > 0
    final_index = path[-1]
    assert arr[final_index] == expected_val


def test_empty_path_on_failure():
    sol = Solution()
    # No zero in this array
    arr = [1, 2, 3]
    path = sol.jump_to_zero(arr, 0)
    assert path == []
