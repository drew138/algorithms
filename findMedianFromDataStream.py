# problem: https://leetcode.com/problems/find-median-from-data-stream/
# Runtime: 376 ms, faster than 20.03% of Python3 online submissions for Find Median from Data Stream.
# Memory Usage: 26 MB, less than 5.47% of Python3 online submissions for Find Median from Data Stream.


from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sl = SortedList()

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        l = len(self.sl)
        if l & 1:
            return self.sl[l // 2]
        else:
            return (self.sl[l//2] + self.sl[l//2 - 1]) / 2
