import pytest
from l00045_jump_game_ii import Solution, Solution2


@pytest.mark.parametrize(
    "nums, expected_jumps",
    [
        # --- LeetCode Example 1 ---
        # 2 -> 3 -> 4 (index 0 to 1, then 1 to 4)
        ([2, 3, 1, 1, 4], 2),
        # --- LeetCode Example 2 ---
        # 2 -> 1 -> 1 (index 0 to 2, then 2 to 4)
        ([2, 3, 0, 1, 4], 2),
        # --- Base Cases ---
        # Already at the end
        ([0], 0),
        ([1], 0),
        ([5, 10], 1),
        # --- Linear Jumps ---
        # 1 -> 1 -> 1 -> 1
        ([1, 1, 1, 1, 1], 4),
        # --- Big Jumps ---
        # Can jump from start to finish immediately
        ([10, 1, 1, 1, 1, 1], 1),
        # --- Zeros in the middle ---
        # Must jump over the zero at index 2
        ([2, 5, 0, 0, 1], 2),
        # --- Maximum possible jumps (staircase) ---
        ([4, 3, 2, 1, 0], 1),  # Using your current DP "infinity"
        # --- Tight Constraints ---
        # Each jump is the minimum required
        ([2, 1, 1, 1, 1], 3),
    ],
)
@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_jump(sol, nums, expected_jumps):
    assert sol.jump(nums) == expected_jumps


@pytest.mark.parametrize("sol", [Solution(), Solution2()])
def test_large_array_performance(sol):
    """
    Optional: Test with a larger array to see if the O(N^2) DP
    implementation holds up or hits a timeout.
    """
    # 1000 elements all with jump value 1
    nums = [1] * 1000
    assert sol.jump(nums) == 999  # n-1 jumps
