# problem: https: // leetcode.com/problems/poor-pigs/
# Runtime: 16 ms, faster than 100.00 % of Python3 online submissions for Poor Pigs.
# Memory Usage: 14 MB, less than 74.29 % of Python3 online submissions for Poor Pigs.


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        import math
        numTests = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets, numTests+1))
