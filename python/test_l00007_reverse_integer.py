# 7 https://leetcode.com/problems/reverse-integer/

import pytest
from l00007_reverse_integer import Solution, Solution2


@pytest.mark.parametrize(
    "x, expected",
    [
        # --- LeetCode Example 1 ---
        (123, 321),
        # --- LeetCode Example 2 ---
        (-123, -321),
        # --- LeetCode Example 3 (Trailing Zero) ---
        (120, 21),
        # --- Zero Case ---
        (0, 0),
        # --- Boundary: Max 32-bit Integer ---
        # 2147483647 -> 7463847412 (Overflows)
        (2147483647, 0),
        # --- Boundary: Min 32-bit Integer ---
        # -2147483648 -> -8463847412 (Overflows)
        (-2147483648, 0),
        # --- Large Input (No Overflow) ---
        # 1147483641 -> 1463847411 (Valid)
        (1147483641, 1463847411),
        # --- The Specific Failure Case (From your screenshot) ---
        # 1534236469 -> 9646324351 (Overflows)
        (1534236469, 0),
        # --- Negative Overflow ---
        # -1563847412 -> -2147483651 (Overflows by 3)
        (-1563847412, 0),
        # --- Single Digit ---
        (5, 5),
        (-5, -5),
    ],
)
@pytest.mark.parametrize("sol_class", [Solution, Solution2])
def test_reverse(sol_class, x, expected):
    sol = sol_class()
    assert sol.reverse(x) == expected
