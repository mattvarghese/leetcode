import pytest
from p__008_hop_time import Solution  # Adjust this import based on your filename


@pytest.fixture
def solver():
    return Solution()


@pytest.mark.parametrize(
    "times, hops, expected",
    [
        # --- 1. The "Short Way is Expensive" Case ---
        # Moving 1 -> 2 (index 0 -> 1).
        # Clockwise (1-2): Exit 1 (Cost 100).
        # Counter-Clockwise (1-5-4-3-2): Exit 1(100) + 5(1) + 4(1) + 3(1). Total 103.
        # Min: 100.
        ([100, 1, 1, 1, 1], [2], 100),
        # --- 2. The "Backwards is Cheaper" Case ---
        # 3 nodes. Moving 1 -> 3.
        # CW: 1->2 (10), 2->3 (10). Total 20.
        # CCW: 1->3 (Exit 1 = 10). Total 10.
        # Min: 10.
        ([10, 10, 10], [3], 10),
        # --- 3. The "Midnight" Wrap-Around (Sequential) ---
        # 1 -> 5: CW (1+1+1+1=4), CCW (Exit 1=1). Min: 1. (Now at 5)
        # 5 -> 2: CW (Exit 5(1) + Exit 1(1) = 2), CCW (Exit 5(1) + 4(1) + 3(1) = 3). Min: 2.
        # Total: 3.
        ([1, 1, 1, 1, 1], [5, 2], 3),
        # --- 4. The "Zig-Zag" Stress Test ---
        # Testing if state 'prevHop' is maintained correctly.
        # times: [2, 3, 10, 1, 4]
        # 1 -> 4: CW(2+3+10=15), CCW(2+4=6). Min: 6. (Now at 4)
        # 4 -> 2: CW(1+4+2=7), CCW(1+10+3=14). Min: 7.
        # Total: 13.
        ([2, 3, 10, 1, 4], [4, 2], 13),
        # --- 5. Large Asymmetric Jump ---
        # Node 3 is a massive bottleneck.
        # 1 -> 4: CW must pass node 3 (2+3+100=105).
        # CCW: 1(2)+5(4)=6.
        # Min: 7.
        ([2, 3, 100, 1, 4], [4], 6),
        # --- 6. Already There ---
        # Moving to current node should cost 0.
        ([10, 20, 30], [1, 1, 3, 3], 10),  # 1->1(0), 1->3(10), 3->3(0)
        # --- 7. Minimal 2-Node Ring ---
        # 1 -> 2: Both directions exit node 1 (Cost 10).
        # 2 -> 1: Both directions exit node 2 (Cost 50).
        # Total: 60.
        ([10, 50], [2, 1], 60),
    ],
)
def test_travel_time(solver, times, hops, expected):
    """
    Validates the circular asymmetric travel time where cost to move
    from node i is times[i] regardless of direction.
    """
    assert solver.minTravelTime(times, hops) == expected
