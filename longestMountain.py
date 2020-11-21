# problem: https://leetcode.com/problems/longest-mountain-in-array/submissions/
# Runtime: 188 ms, faster than 18.37% of Python3 online submissions for Longest Mountain in Array.
# Memory Usage: 15.5 MB, less than 11.78% of Python3 online submissions for Longest Mountain in Array.

from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        longestMnt = 0
        lenArr = len(A)
        if lenArr < 3:
            return longestMnt
        peaks = []
        valleys = set()
        for i, val in enumerate(A):
            isPeak = i != 0 and i != (lenArr - 1) and (A[i-1] < val > A[i+1])
            if isPeak:
                peaks.append(i)
        for i, val in enumerate(A):
            condOne = (i == 0 and A[i+1] >= val) or (i ==
                                                     (lenArr - 1) and A[i-1] >= val)
            condTwo = (i != 0 and i != (lenArr - 1)
                       ) and (A[i-1] >= val <= A[i+1])
            isValley = condOne or condTwo
            if isValley:
                valleys.add(i)
        if peaks:
            longestMnt = 3
        for i, val in enumerate(peaks):
            x, y = val - 1, val + 1
            count = 3
            while not x in valleys or not y in valleys:
                if not x in valleys:
                    x -= 1
                    count += 1
                    longestMnt = max(longestMnt, count)
                if not y in valleys:
                    y += 1
                    count += 1
                    longestMnt = max(longestMnt, count)

        return longestMnt


Solution().longestMountain([40, 51, 29, 19, 50, 25])
