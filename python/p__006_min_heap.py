class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        # 1. Add to the end
        self.heap.append(val)
        # 2. Fix the heap property by moving up
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # 1. Swap root with last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        # 2. Fix the heap property by moving down
        self._sift_down(0)
        return root

    def _sift_up(self, index):
        parent = (index - 1) // 2
        # If we aren't at root and current is smaller than parent...
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)

    def _sift_down(self, index):
        small = index
        left, right = 2 * index + 1, 2 * index + 2

        # Find the smallest among parent and two children
        if left < len(self.heap) and self.heap[left] < self.heap[small]:
            small = left
        if right < len(self.heap) and self.heap[right] < self.heap[small]:
            small = right

        # If a child was smaller, swap and keep sifting down
        if small != index:
            self.heap[index], self.heap[small] = self.heap[small], self.heap[index]
            self._sift_down(small)
