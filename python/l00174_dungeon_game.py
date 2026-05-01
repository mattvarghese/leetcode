# 174 - https://leetcode.com/problems/dungeon-game/

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        if m == 0:
            return 0
        n = len(dungeon[0])
        if n == 0:
            return 0
        costs = [9999] * (n - 1) + [1] * 2
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                costDown = costs[j] - dungeon[i][j]
                costRight = costs[j + 1] - dungeon[i][j]
                costs[j] = min(costDown, costRight)
                if costs[j] < 1:
                    costs[j] = 1
            # After the first row (bottom), the 'dummy' value at dp[n]
            # must remain Infinity so the next row's rightmost cell
            # can't "exit" right.
            costs[n] = 9999
        return costs[0]
