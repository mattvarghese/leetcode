import os
import sys

import pytest

# Add the current directory to sys.path so importlib can find the file
sys.path.append(os.path.dirname(__file__))
# Note - the above bleeds to all tests, which is why we don't need this in
# every test file we have in this folder.
# But this fails if you try to run a single test-case by itself

from .e00007_nth_prime import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 2),  # First prime
        (2, 3),  # Second prime
        (3, 5),  # Third prime
        (6, 13),  # Boundary case (our formula logic kicks in at n=6)
        (10, 29),  # Small n
        (100, 541),  # Medium n
        (1000, 7919),  # Large n
        (10001, 104743),  # Project Euler Goal
    ],
)
def test_get_nth_prime_valid(solution, n, expected):
    """Test standard valid inputs for the nth prime."""
    assert solution.get_nth_prime(n) == expected


@pytest.mark.parametrize("n", [(0), (-1), (-100)])
def test_get_nth_prime_invalid(solution, n):
    """Verify that non-positive inputs return None."""
    assert solution.get_nth_prime(n) is None
