# https://leetcode.com/problems/combinations/

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = []
        self.pick_recurse(1, n, 1, k, [], result)
        return result

    def pick_recurse(
        self,
        start: int,
        n: int,
        pos: int,
        k: int,
        current: List[int],
        result: List[List[int]],
    ):
        if pos == k + 1:
            result.append(current[:])
        else:
            for i in range(start, n + 1):
                current.append(i)
                self.pick_recurse(i + 1, n, pos + 1, k, current, result)
                current.pop()
