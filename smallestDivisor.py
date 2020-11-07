# problem: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/submissions/
# Runtime: 452 ms, faster than 49.66% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.
# Memory Usage: 19.8 MB, less than 80.03% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        import math
        divisor = 1
        max_num = 1000000
        while divisor <= max_num:
            mid = math.floor(divisor + ((max_num - divisor) / 2))
            total = sum([math.ceil(x/mid) for x in nums])
            if total > threshold:
                divisor = mid + 1
            else:
                max_num = mid - 1
        return divisor
