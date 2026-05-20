from collections import deque


class MaxSlidingWindow:
    def __init__(self, nums: list[int]):
        self._nums, self._len = nums, len(nums)
        self._largeIx: deque[int] = deque()
        self._largeIx.append(0)
        self._left, self._right = 0, 0

    def getMax(self) -> int:
        return self._nums[self._largeIx[0]]

    def expandRight(self):
        if self._right < self._len - 1:
            self._right += 1
            value = self._nums[self._right]
            while (len(self._largeIx) > 0) and (self._nums[self._largeIx[-1]] < value):
                self._largeIx.pop()
            self._largeIx.append(self._right)

    def contractLeft(self):
        if (self._left <= self._right) and (self._left < self._len - 1):
            if self._left == self._largeIx[0]:
                self._largeIx.popleft()
            self._left += 1
            if self._left > self._right:
                self.expandRight()
