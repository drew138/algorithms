# problem: https: // leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
# Runtime: 416 ms, faster than 68.66% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
# Memory Usage: 28.6 MB, less than 91.60% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.

from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        from collections import Counter
        counter = Counter(nums)
        nums.sort()
        n = len(nums)
        if n % k != 0:
            return False
        for num in nums:
            if counter[num]:
                n = k - 1
                counter[num] -= 1
                while n:
                    if counter[num+n]:
                        counter[num+n] -= 1
                    else:
                        return False
                    n -= 1
        return True
