# problem: https://leetcode.com/problems/koko-eating-bananas/
# Runtime: 875 ms, faster than 13.15% of Python3 online submissions for Koko Eating Bananas.
# Memory Usage: 15.6 MB, less than 18.51% of Python3 online submissions for Koko Eating Bananas.

from typing import List
import math

class Solution:
    def satisfies_hours(self, piles, h, k):
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
        return total <= h
        
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 10 ** 9 + 1
        
        while l < r:
            mid = (r - l) // 2 + l
            if self.satisfies_hours(piles, h, mid):
                r = mid
            else:
                l = mid + 1
        return l
        
        