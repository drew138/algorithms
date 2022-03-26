# problem: https://leetcode.com/problems/binary-search/
# Runtime: 329 ms, faster than 49.60% of Python3 online submissions for Binary Search.
# Memory Usage: 15.6 MB, less than 5.21% of Python3 online submissions for Binary Search.


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = ((r - l) // 2) + l
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l if nums[l] == target else -1