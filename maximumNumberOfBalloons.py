# problem: https://leetcode.com/problems/maximum-number-of-balloons/
# Runtime: 20 ms, faster than 99.49% of Python3 online submissions for Maximum Number of Balloons.
# Memory Usage: 14.4 MB, less than 20.82% of Python3 online submissions for Maximum Number of Balloons.


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        counter = Counter(text)
        b = counter["b"]
        a = counter["a"]
        l = counter["l"] // 2
        o = counter["o"] // 2
        n = counter["b"]
        return min(b, a, l, o, n)
