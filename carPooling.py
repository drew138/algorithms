# problem: https://leetcode.com/problems/car-pooling/
# Runtime: 90 ms, faster than 25.24% of Python3 online submissions for Car Pooling.
# Memory Usage: 15.4 MB, less than 18.85% of Python3 online submissions for Car Pooling.

from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from sortedcontainers import SortedList
        passengers = SortedList()
        trips.sort(key=lambda x: x[1])
        for num, from_, to in trips:
            while passengers and passengers[0][0] <= from_:
                _, b = passengers.pop(0)
                capacity += b
            capacity -= num
            passengers.add((to, num))
            if capacity < 0:
                return False
        return True