# problem: https://leetcode.com/problems/contains-duplicate-iii/
# Runtime: 1004 ms, faster than 6.11% of Python3 online submissions for Contains Duplicate III.
# Memory Usage: 17.2 MB, less than 89.59% of Python3 online submissions for Contains Duplicate III.

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from sortedcontainers import SortedList
        window = SortedList()

        for i, val in enumerate(nums):
            if i - k > 0:
                idx = window.index(nums[i - k - 1])
                window.pop(idx)

            window.add(val)
            j = window.index(val)
            if j - 1 >= 0 and abs(window[j-1] - val) <= t:
                return True
            if j + 1 < len(window) and abs(window[j+1] - val) <= t:
                return True
        return False
