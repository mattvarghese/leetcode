# Cost to move from i to either i+1 or to i-1 is times[i]
# Starting at index 1, get total time to travel the path in hops array.
#
# Note: indices are starting at 1 in the problem - hence we make hops2 array


class Solution:
    def minTravelTime(self, times: list[int], hops: list[int]) -> int:
        m = len(times)
        hops2 = [(hop - 1) for hop in hops]  # Adjust for indices starting at 1
        cumForwardTimes = [0] * (m + 1)
        cumBackwardTimes = [0] * m
        for i in range(m):
            cumForwardTimes[i + 1] = cumForwardTimes[i] + times[i]
        cumBackwardTimes[m - 1] = times[0]
        for i in range(m - 2, -1, -1):
            cumBackwardTimes[i] = cumBackwardTimes[i + 1] + times[i + 1]
        totalTime, prevHop = 0, 0
        for hop in hops2:
            if hop == prevHop:
                continue  # time added is 0, prevHop is already hop
            elif hop > prevHop:
                forwardTime = cumForwardTimes[hop] - cumForwardTimes[prevHop]
                backwardTime = (
                    cumBackwardTimes[0]
                    - cumBackwardTimes[prevHop]
                    + cumBackwardTimes[hop]
                )
                totalTime += min(forwardTime, backwardTime)
            else:
                forwardTime = (
                    cumForwardTimes[m] - cumForwardTimes[prevHop] + cumForwardTimes[hop]
                )
                backwardTime = cumBackwardTimes[hop] - cumBackwardTimes[prevHop]
                totalTime += min(forwardTime, backwardTime)
            prevHop = hop
        return totalTime
