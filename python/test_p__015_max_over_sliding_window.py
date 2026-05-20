import pytest
from p__015_max_over_sliding_window import MaxSlidingWindow


@pytest.fixture
def create_window():
    """
    Factory fixture to instantiate the window solver with a given sequence.
    """

    def _init_solver(nums: list[int]) -> MaxSlidingWindow:
        return MaxSlidingWindow(nums)

    return _init_solver


@pytest.mark.parametrize(
    "nums, actions, expected_maxes",
    [
        # --- 1. Long Saw-Tooth Wave Pattern ---
        # Tests continuous up-and-down oscillations where the deque must
        # repeatedly dump partial tails but preserve historical peaks.
        (
            [12, 5, 18, 3, 22, 1, 14, 9, 25, 4],
            [
                "E",
                "E",
                "E",
                "E",
                "E",  # Expand to index 5: [12, 5, 18, 3, 22, 1] -> Max 22
                "C",
                "C",
                "C",  # Contract left x3: window is now indices 3-5 [3, 22, 1] -> Max 22
                "E",
                "E",
                "E",
                "E",  # Expand to index 9: [3, 22, 1, 14, 9, 25, 4] -> Max 25
                "C",
                "C",
                "C",
                "C",
                "C",  # Contract left x5: window is indices 8-9 [25, 4] -> Max 25
            ],
            [12, 18, 18, 22, 22, 22, 22, 22, 22, 22, 25, 25, 25, 25, 25, 25, 25],
        ),
        # --- 2. Micro-Step Oscillations (Size 1 to 2 Jumps) ---
        # Rapid contract-expand sequences forcing the window to constantly
        # cross its own boundary and trigger your `self.expandRight()` catch-up logic.
        (
            [100, 20, 80, 10, 90, 30, 70],
            [
                "C",
                "E",  # [0]->[1](20) via catchup -> [1..2](20, 80) -> Max 80
                "C",
                "E",  # [1..2]->[2](80) -> [2..3](80, 10) -> Max 80
                "C",
                "E",  # [2..3]->[3](10) -> [3..4](10, 90) -> Max 90
                "C",
                "C",  # [3..4]->[4](90) -> [5](30) via catchup -> [5](30) terminal block protection
            ],
            [20, 80, 80, 80, 10, 90, 90, 30],
        ),
        # --- 3. Plateaus and Trailing Plateaus ---
        # Large sequences of repeating maximums to ensure strict inequality prevents
        # the deque from losing track of identical adjacent values when left contracts.
        (
            [7, 7, 7, 3, 3, 7, 7],
            [
                "E",
                "E",
                "E",
                "E",  # [0..4] -> [7, 7, 7, 3, 3] -> Max 7
                "C",
                "C",
                "C",  # Contract 3 times -> [3..4] -> [3, 3] -> Max 3
                "E",
                "E",  # Expand to end -> [3..6] -> [3, 3, 7, 7] -> Max 7
                "C",
                "C",
                "C",  # Contract down to final element -> [6..6] -> [7] -> Max 7
            ],
            [7, 7, 7, 7, 7, 7, 3, 7, 7, 7, 7, 7],
        ),
        # --- 4. Deep Terminal Stall Assault ---
        # Hits the absolute end of the array early, then bombards `contractLeft`
        # with twice as many calls as there are elements to guarantee the short-circuit remains a absolute no-op.
        (
            [50, 10, 30],
            [
                "E",
                "E",  # Expand to end: [50, 10, 30] -> Max 50
                "C",  # Drop index 0: [10, 30] -> Max 30
                "C",  # Drop index 1: [30] -> Max 30 (Window size 1 at terminal index)
                "C",
                "C",
                "C",
                "C",  # Redundant loops past len-1 boundary
            ],
            [50, 50, 30, 30, 30, 30, 30, 30],
        ),
        # --- 5. Step-Through Symmetrical Valley ---
        # Window starts large, captures a valley (high, low, high), shrinks down to the absolute bottom,
        # and then expands out to capture the next peak.
        (
            [15, 2, 1, 0, 1, 2, 20],
            [
                "E",
                "E",
                "E",
                "E",
                "E",  # [15, 2, 1, 0, 1, 2] -> Max 15
                "C",
                "C",
                "C",  # Drop 15, 2, 1 -> [0, 1, 2] -> Max 2
                "C",
                "C",  # Drop 0, 1 -> [2] -> Max 2
                "E",  # Capture peak -> [2, 20] -> Max 20
            ],
            [15, 15, 15, 15, 15, 2, 2, 2, 2, 2, 20],
        ),
    ],
)
def test_sliding_window_stream(
    create_window, nums: list[int], actions: list[str], expected_maxes: list[int]
) -> None:
    """
    Verifies state tracking accuracy across custom-sequenced window manipulations.
    'E' triggers expandRight(), 'C' triggers contractLeft().
    """
    window = create_window(nums)
    results = []

    for action in actions:
        if action == "E":
            window.expandRight()
        elif action == "C":
            window.contractLeft()

        results.append(window.getMax())

    assert results == expected_maxes


def test_initial_state(create_window) -> None:
    """
    Verifies that the window initializes as a valid single-element sequence
    pointing cleanly to the zero-index primitive.
    """
    nums = [7, 12, 4]
    window = create_window(nums)
    assert window.getMax() == 7


def test_terminal_no_op_invariants(create_window) -> None:
    """
    Explicitly targets your boundary condition rule: contracting a size-1
    window at the terminal element must short-circuit into a safe no-op.
    """
    nums = [10, 5, 25]
    window = create_window(nums)

    window.expandRight()  # right=1
    window.expandRight()  # right=2
    window.contractLeft()  # left=1
    window.contractLeft()  # left=2

    assert window.getMax() == 25

    # Fire redundant contractions out of bounds
    window.contractLeft()
    window.contractLeft()

    # Invariant: Pointers must not corrupt or throw IndexError
    assert window.getMax() == 25
