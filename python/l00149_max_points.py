# https://leetcode.com/problems/max-points-on-a-line/

import math
from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        max_points = 0
        for i in range(n):
            # if max_points >= n - i:
            #    break

            slopes = defaultdict(int)
            x1, y1 = points[i]
            duplicates = 1  # The point itself
            i_max = 0

            for j in range(i + 1, n):
                # if max_points >= (i_max + n - j):
                #    break

                x2, y2 = points[j]

                dx, dy = x2 - x1, y2 - y1

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                if dy == 0:
                    dx = 1
                elif dx == 0:
                    dy = 1
                else:
                    if dx < 0:
                        dx, dy = -dx, -dy
                    g = abs(math.gcd(dx, dy))
                    dx = dx // g
                    dy = dy // g
                slope = (dx, dy)

                slopes[slope] += 1
                i_max = max(i_max, slopes[slope])

            max_points = max(max_points, i_max + duplicates)

        return max_points
