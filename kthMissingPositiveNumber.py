# problem: https://leetcode.com/problems/kth-missing-positive-number/
# Runtime: 40 ms, faster than 98.63% of Python3 online submissions for Kth Missing Positive Number.
# Memory Usage: 14.4 MB, less than 35.70% of Python3 online submissions for Kth Missing Positive Number.


from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        if l == r:
            mid = 0
        while l < r:
            mid = l + ((r - l) // 2)
            if arr[mid] - (mid + 1) < k:
                mid += 1
                l = mid
            else:
                r = mid
        base = k + mid - arr[mid] if arr[mid] - \
            (mid + 1) >= k else k + 1 + mid - arr[mid]
        return (arr[mid] + base)
