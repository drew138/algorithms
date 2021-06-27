# problem: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# Runtime: 2584 ms, faster than 82.65% of Python3 online submissions for Count of Smaller Numbers After Self.
# Memory Usage: 32.1 MB, less than 88.67% of Python3 online submissions for Count of Smaller Numbers After Self.

from sortedcontainers import SortedList
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        answer = []
        for i in range(len(nums)-1, -1, -1):
            n = SortedList.bisect_left(sl, nums[i])
            answer.append(n)
            sl.add(nums[i])
        return reversed(answer)
