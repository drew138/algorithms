# problem: https://leetcode.com/problems/jewels-and-stones/
# Runtime: 20 ms, faster than 98.96% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14.2 MB, less than 39.74% of Python3 online submissions for Jewels and Stones.


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stones.count(j) for j in jewels)
