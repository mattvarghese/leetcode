# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from collections import deque
from enum import Enum
from typing import List, Optional


class AVLTreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # AVL trees need to track height


class AVLTree:
    def get_height(self, node: Optional[AVLTreeNode]) -> int:
        return node.height if node else 0

    def get_balance(self, node: Optional[AVLTreeNode]) -> int:
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y: AVLTreeNode) -> AVLTreeNode:
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x: AVLTreeNode) -> AVLTreeNode:
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root: Optional[AVLTreeNode], key: int) -> AVLTreeNode:
        # 1. Standard BST insertion
        if not root:
            return AVLTreeNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get balance factor and perform rotations if needed
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.val:
            return self.rotate_right(root)
        # Right Right Case
        if balance < -1 and key > root.right.val:
            return self.rotate_left(root)
        # Left Right Case
        if balance > 1 and key > root.left.val:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # Right Left Case
        if balance < -1 and key < root.right.val:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root


class AVLSolution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[AVLTreeNode]:
        if not nums:
            return None

        # Using a queue to process elements one by one
        queue = deque(nums)
        avl = AVLTree()
        root = None

        while queue:
            val = queue.popleft()  # Getting first element
            root = avl.insert(root, val)

        return root


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Step 1: Ensure sorting (if not guaranteed by problem)
        # nums.sort()

        return self._build(nums, 0, len(nums) - 1)

    def _build(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        # Step 2: Pick the middle element as the root
        mid = (left + right) // 2
        root = TreeNode(nums[mid])

        # Step 3: Recursively build the subtrees
        root.left = self._build(nums, left, mid - 1)
        root.right = self._build(nums, mid + 1, right)

        return root


class Color(Enum):
    RED = 1
    BLACK = 2


class RBNode:
    def __init__(self, val: int, color: Color = Color.RED):
        self.val = val
        self.color = color
        self.left: Optional[RBNode] = None
        self.right: Optional[RBNode] = None
        self.parent: Optional[RBNode] = None


class SolutionRedBlack:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[RBNode]:
        if not nums:
            return None

        self.root = None
        for val in nums:
            self.insert(val)
        return self.root

    def rotate_left(self, x: RBNode):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, y: RBNode):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, val: int):
        new_node = RBNode(val)

        # Standard BST Insert
        y = None
        x = self.root
        while x:
            y = x
            if new_node.val < x.val:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if not y:
            self.root = new_node
        elif new_node.val < y.val:
            y.left = new_node
        else:
            y.right = new_node

        self._fix_insert(new_node)

    def _fix_insert(self, k: RBNode):
        while k.parent and k.parent.color == Color.RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle
                if u and u.color == Color.RED:
                    # Case 1: Uncle is red (Color Flip)
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Case 2: Uncle is black, k is left child
                        k = k.parent
                        self.rotate_right(k)
                    # Case 3: Uncle is black, k is right child
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self.rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right  # Uncle
                if u and u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self.rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = Color.BLACK
