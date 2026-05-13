class HeapSort:
    def __init__(self, data, mode="max"):
        """
        Maintains an internal heap.
        Note: Max-Heap + Ascending Sort is the default.
        """
        self.heap = data
        self.mode = mode.lower()
        self.n = len(data)
        self._build_heap()

    def _get_parent(self, i):
        """
        ASSUMPTION: 0-based indexing.
        The parent of index i is always at (i-1)//2.
        Example: Indices 1 and 2 both have parent 0.
        """
        return (i - 1) // 2

    def _get_children(self, i):
        """
        ASSUMPTION: A complete binary tree filled level by level.
        Left child: 2i + 1
        Right child: 2i + 2
        """
        return 2 * i + 1, 2 * i + 2

    def _compare(self, parent_idx, child_idx):
        """
        Determines if the 'Heap Property' is violated based on the mode.
        Max-Heap: Parent must be >= Child.
        Min-Heap: Parent must be <= Child.
        """
        p_val = self.heap[parent_idx]
        c_val = self.heap[child_idx]
        if self.mode == "max":
            return p_val < c_val  # Violates Max-Heap if parent is smaller
        else:
            return p_val > c_val  # Violates Min-Heap if parent is larger

    def _sift_down(self, i, limit):
        """
        Moves an element down the tree until it satisfies the heap property.
        ASSUMPTION: We only consider indices up to 'limit' to allow
        the sort() method to 'shrink' the heap.
        """
        while True:
            left, right = self._get_children(i)
            target = i

            # Check if left child exists and violates property
            if left < limit and self._compare(target, left):
                target = left

            # Check if right child exists and is even 'more' of a violation
            # (e.g., in max-heap, is right child bigger than left?)
            if right < limit and self._compare(target, right):
                target = right

            if target != i:
                # Swap and continue sifting down from the new position
                self.heap[i], self.heap[target] = self.heap[target], self.heap[i]
                i = target
            else:
                # Property satisfied
                break

    def _build_heap(self):
        """
        ASSUMPTION: All nodes from n//2 to n are leaf nodes.
        Leaf nodes satisfy the heap property by default (they have no children).
        Therefore, we only need to sift down from the last non-leaf node up to the root.
        This makes heap construction O(n) instead of O(n log n).
        """
        for i in range((self.n // 2) - 1, -1, -1):
            self._sift_down(i, self.n)

    def sort(self):
        """Standard in-place sort. Mutates self.heap."""
        for i in range(self.n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self._sift_down(0, i)
        return self.heap

    def __iter__(self):
        """
        Iterates through the elements in SORTED order.
        Note: This implementation is 'destructive' to the heap structure
        to maintain O(1) extra space during iteration.
        """
        # We perform the sort logic but yield each element as it's 'locked'
        # We work backwards to yield in ascending order for a Max-Heap

        # 1. Fully sort the array first
        self.sort()

        # 2. Yield the now-sorted elements
        for item in self.heap:
            yield item
