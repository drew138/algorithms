# problem: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Runtime: 329 ms, faster than 14.17% of Python3 online submissions for Kth Largest Element in a Stream.
# Memory Usage: 18.3 MB, less than 31.19% of Python3 online submissions for Kth Largest Element in a Stream.


from sortedcontainers import SortedList
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = SortedList()
        self.k = k
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if self.pq and val > self.pq[0] and len(self.pq) == self.k:
            self.pq.pop(0)
        if len(self.pq) < self.k:
            self.pq.add(val)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)