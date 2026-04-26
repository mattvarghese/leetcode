# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import math

import pytest
from l00108_balanced_bst import AVLSolution, Solution, SolutionRedBlack


def inOrder(node, res):
    if not node:
        return
    inOrder(node.left, res)
    res.append(node.val)
    inOrder(node.right, res)


def get_height(node):
    if not node:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))


def is_balanced(node):
    """Strict AVL balance check: height difference <= 1."""
    if not node:
        return True
    left_h = get_height(node.left)
    right_h = get_height(node.right)
    return (
        abs(left_h - right_h) <= 1
        and is_balanced(node.left)
        and is_balanced(node.right)
    )


def is_rb_balanced(node, n):
    """
    Relaxed Red-Black balance check.
    A Red-Black tree guarantees height <= 2 * log2(n + 1).
    """
    if n == 0:
        return node is None
    height = get_height(node)
    # The maximum height of a Red-Black tree with n nodes
    max_allowed_height = 2 * math.log2(n + 1)
    return height <= max_allowed_height


@pytest.mark.parametrize(
    "nums",
    [
        ([-10, -3, 0, 5, 9]),
        ([1, 3]),
        ([1, 2, 3, 4, 5, 6, 7]),
    ],
)
@pytest.mark.parametrize("sol", [Solution(), AVLSolution(), SolutionRedBlack()])
def test_sorted_array_to_bst(sol, nums):
    root = sol.sortedArrayToBST(nums)

    # 1. Verify BST property (In-order must be sorted)
    res = []
    inOrder(root, res)
    assert res == nums

    # 2. Verify Balance property based on implementation architecture
    if isinstance(sol, SolutionRedBlack):
        # Use the Red-Black specific height guarantee
        assert is_rb_balanced(root, len(nums))
    else:
        # Use strict AVL balancing for Solution and AVLSolution
        assert is_balanced(root)
