# problem: https://leetcode.com/problems/powerful-integers/solution/
# Runtime: 32 ms, faster than 69.17% of Python3 online submissions for Powerful Integers.
# Memory Usage: 14.4 MB, less than 30.42% of Python3 online submissions for Powerful Integers.

from typing import List
import math


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        answer = set()
        xBound = int(math.log(bound, x) // 1) if x > 1 else 1
        yBound = int(math.log(bound, y) // 1) if y > 1 else 1
        for i in range(xBound + 1):
            for j in range(yBound + 1):
                if x ** i + y ** j <= bound:
                    answer.add(x ** i + y ** j)
        return list(answer)
