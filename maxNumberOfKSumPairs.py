# problem: https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Runtime: 644 ms, faster than 89.46 % of Python3 online submissions for Max Number of K-Sum Pairs.
# Memory Usage: 27.1 MB, less than 71.19 % of Python3 online submissions for Max Number of K-Sum Pairs.

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        m = {}
        answer = 0
        for num in nums:
            if ((k - num) in m) and m[(k-num)]:
                answer += 1
                m[(k-num)] -= 1
            elif num in m:
                m[num] += 1
            else:
                m[num] = 1
        return answer
