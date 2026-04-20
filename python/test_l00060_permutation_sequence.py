import os
import sys

import pytest

# Add the current directory to sys.path so pytest can find the module
sys.path.append(os.path.dirname(__file__))

from l00060_permutation_sequence import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "n, k, expected",
    [
        # --- LeetCode Official Examples ---
        (3, 3, "213"),  # Example 1
        (4, 9, "2314"),  # Example 2
        (3, 1, "123"),  # Example 3
        # --- Edge Cases & Constraints ---
        (1, 1, "1"),  # Minimum n
        (2, 1, "12"),  # Smallest k
        (2, 2, "21"),  # Largest k for n=2
        (3, 6, "321"),  # Largest k for n=3 (n!)
        (9, 1, "123456789"),  # Start of largest n range
        (9, 362880, "987654321"),  # End of largest n range (9!)
    ],
)
def test_get_permutation(sol, n, k, expected):
    """
    Verifies that the k-th permutation matches the expected lexicographical string.
    """
    result = sol.getPermutation(n, k)
    assert result == expected, (
        f"Failed for n={n}, k={k}: expected {expected}, got {result}"
    )


def test_permutation_integrity(sol):
    """
    Verify that the result is actually a permutation of the numbers 1..n.
    """
    n, k = 5, 16
    result = sol.getPermutation(n, k)

    # 1. Check length
    assert len(result) == n

    # 2. Check that all digits from 1 to n are present
    digits = sorted([int(d) for d in result])
    assert digits == list(range(1, n + 1))
