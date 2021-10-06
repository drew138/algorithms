# problem: https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Runtime: 340 ms, faster than 90.81% of Python3 online submissions for Find All Duplicates in an Array.
# Memory Usage: 23.8 MB, less than 5.36% of Python3 online submissions for Find All Duplicates in an Array.

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        seen = set()
        for num in nums:
            if num in seen:
                answer.append(num)
            else:
                seen.add(num)
        return answer
