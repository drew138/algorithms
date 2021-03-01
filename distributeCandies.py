# problem: https://leetcode.com/problems/distribute-candies/
# Runtime: 772 ms, faster than 92.26% of Python3 online submissions for Distribute Candies.
# Memory Usage: 16.3 MB, less than 66.24% of Python3 online submissions for Distribute Candies.

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return int(min(len(candyType)/2, len(set(candyType))))
