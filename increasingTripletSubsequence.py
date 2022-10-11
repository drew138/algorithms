# problem: https://leetcode.com/problems/increasing-triplet-subsequence/
# Runtime: 588 ms, faster than 93.05% of Python3 online submissions for Increasing Triplet Subsequence.
# Memory Usage: 24.7 MB, less than 49.03% of Python3 online submissions for Increasing Triplet Subsequence.from typing import List

import bisect
import math
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second, third = math.inf, math.inf, math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            elif num <= third:
                third = num

        return first < second < third and (third != math.inf)


# Alternate solution O(nlogn)
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#
#         tmp = [nums[0]]
#         for num in nums:
#             if num > tmp[-1]:
#                 tmp.append(num)
#             else:
#                 index = bisect.bisect_left(tmp, num)
#                 tmp[index] = num
#
#         return len(tmp) >= 3
