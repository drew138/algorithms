# problem: https://leetcode.com/problems/find-k-closest-elements/
# Runtime: 320 ms, faster than 40.91% of Python3 online submissions for Find K Closest Elements.
# Memory Usage: 15.7 MB, less than 24.45% of Python3 online submissions for Find K Closest Elements.


from typing import List


class Solution:
    def getLeft(self, arr, l):
        if l < 0:
            return -float("inf")
        return arr[l]

    def getRight(self, arr, r):
        if r >= len(arr):
            return float("inf")
        return arr[r]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from collections import deque
        l, r = 0, len(arr)
        queue = deque()
        while l < r:
            mid = ((r - l) // 2) + l
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        if abs(x - self.getLeft(arr, l - 1)) <= abs(self.getRight(arr, r) - x):
            queue.append(arr[l-1])
            l -= 2
        else:
            queue.append(arr[l])
            l -= 1
            r += 1
        while k := k-1:
            if abs(x - self.getLeft(arr, l)) > abs(self.getRight(arr, r) - x):
                queue.append(arr[r])
                r += 1
            else:
                queue.appendleft(arr[l])
                l -= 1
        return list(queue)
