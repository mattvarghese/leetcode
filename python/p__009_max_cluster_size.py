# Inputs:
#   bootPower: array, where bootPower[i] is the power to boot processor i
#   processingPower: array, where processingPower[i] is the power consumption for processing
#   maxPower: an upper limit
#
# Find the largest number of processors that can form a cluster.
# You only need to return the count / number - not the indices
# Only consecutive processors can form cluster. So 2,3,4,5 is legal, but not 1,3,7
# processors i -> i+k-1 can form a cluster of size k iff:
#   ((max(bootPower[i]...bootPower[i+k-1]) * k) + (sum(processingPower[i]...processingPower[i+k-1]))) < maxPower


from collections import deque


class Solution:
    def maxClusterSize(
        self, bootPower: list[int], processingPower: list[int], maxPower: int
    ) -> int:

        n = len(bootPower)
        if len(processingPower) != n:
            return 0  # Bad inputs

        maxCluster, left, right = 0, 0, 0
        leftMoved, rightMoved = False, True
        sumProcessingWindow = 0

        # We must store indices, and not the boot power values in the dequeue
        # This is because, say we have [10,10,5]
        # Then, the deque will only hold one 10.
        # But if we popleft when the left moves past first 10, we're in error
        maxBootIxDq = deque()

        while left <= right and right < n:
            if leftMoved:
                sumProcessingWindow -= processingPower[left - 1]
                if maxBootIxDq[0] == left - 1:
                    maxBootIxDq.popleft()

            if rightMoved:
                sumProcessingWindow += processingPower[right]
                while maxBootIxDq and bootPower[maxBootIxDq[-1]] <= bootPower[right]:
                    maxBootIxDq.pop()
                maxBootIxDq.append(right)

            windowSize = right - left + 1
            thisPower = (bootPower[maxBootIxDq[0]] * windowSize) + sumProcessingWindow

            if thisPower <= maxPower:
                if windowSize > maxCluster:
                    maxCluster = windowSize
                right += 1
                leftMoved, rightMoved = False, True
            else:
                left += 1
                leftMoved = True
                if left > right:
                    right += 1
                    rightMoved = True
                else:
                    rightMoved = False

        return maxCluster
