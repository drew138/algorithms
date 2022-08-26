# problem: https: // leetcode.com/problems/reordered-power-of-2/
# Runtime: 53 ms, faster than 65.24% of Python3 online submissions for Reordered Power of 2.
# Memory Usage: 13.9 MB, less than 64.17% of Python3 online submissions for Reordered Power of 2.

import math

class Solution:
    def is_answer(self, n, num):
        if num % 10 == 0: return False
        counter_n = [0] * 10
        counter_num = [0] * 10
        while n:
            tmp = n % 10
            n //=10
            counter_n[tmp] += 1
        while num:
            tmp = num % 10
            num //=10
            counter_num[tmp] += 1
        for i in range(10):
            if counter_n[i] != counter_num[i]:
                return False
        return True

    def reorderedPowerOf2(self, n: int) -> bool:
        num = int(math.log10(n))

        cur = math.ceil(math.log2(10** num))
        while 2 ** cur < 10 ** (num + 1):
            if self.is_answer(n, 2 ** cur):
                return True
            cur += 1


        return False
