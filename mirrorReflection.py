# problem: https: // leetcode.com/problems/mirror-reflection/submissions/
# Runtime: 24 ms, faster than 91.58 % of Python3 online submissions for Mirror Reflection.
# Memory Usage: 14.1 MB, less than 31.23 % of Python3 online submissions for Mirror Reflection.


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        ext = q
        ref = p
        while ext % 2 == 0 and ref % 2 == 0:
            ext /= 2
            ref /= 2
        if ext % 2 == 0 and ref % 2 == 1:
            return 0
        elif ext % 2 == 1 and ref % 2 == 0:
            return 2
        elif ext % 2 == 1 and ref % 2 == 1:
            return 1
