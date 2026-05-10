import pytest
from p__009_max_cluster_size import Solution


@pytest.fixture
def solver():
    return Solution()


@pytest.mark.parametrize(
    "bootPower, processingPower, maxPower, expected",
    [
        # --- 1. Standard Case ---
        # Cluster [3, 4, 5] (size 3):
        # Max boot: 15. Sum processing: (2+1+1) = 4.
        # (15 * 3) + 4 = 49. (49 <= 50)
        ([10, 15, 12, 8, 5], [4, 2, 1, 1, 10], 50, 3),
        # --- 2. Single Processor Cluster ---
        # Only the 3rd processor (8, 1) fits: (8*1) + 1 = 9 <= 10.
        ([12, 15, 8, 20], [10, 10, 1, 10], 10, 1),
        # --- 3. No Cluster Possible ---
        # Every processor exceeds maxPower on its own.
        ([50, 60], [10, 10], 40, 0),
        # --- 4. All Processors Form One Cluster ---
        # (5 * 4) + (1+1+1+1) = 24 <= 25.
        ([5, 5, 5, 5], [1, 1, 1, 1], 25, 4),
        # --- 5. Tight Constraint / Boundary ---
        # A cluster of 2 works exactly at the limit.
        ([10, 10], [5, 5], 30, 2),  # (10*2) + 10 = 30.
        # --- 6. Empty or Mismatched Input ---
        ([], [], 100, 0),
        ([10], [10, 20], 100, 0),
    ],
)
def test_max_cluster_size(solver, bootPower, processingPower, maxPower, expected):
    """
    Validates the sliding window logic for processor clusters.
    Equation: (max(boot) * k) + sum(processing) < maxPower
    """
    assert solver.maxClusterSize(bootPower, processingPower, maxPower) == expected
