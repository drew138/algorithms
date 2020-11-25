
# https://leetcode.com/problems/smallest-integer-divisible-by-k/submissions/
# Runtime: 1968 ms, faster than 34.52% of Python3 online submissions for Smallest Integer Divisible by K.
# Memory Usage: 14.3 MB, less than 50.60% of Python3 online submissions for Smallest Integer Divisible by K.

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        mult = 1
        units = set()
        unit = (mult * K) % 10
        while not unit in units:
            units.add(unit)
            mult += 1
            unit = (mult * K) % 10
        if not 1 in units:
            return -1
        unit = 1
        total = 1
        while unit % K != 0:
            unit *= 10
            unit += 1
            total += 1
        return total
