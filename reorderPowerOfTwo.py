# problem: https: // leetcode.com/problems/reordered-power-of-2/
# Runtime: 4028 ms, faster than 5.24 % of Python3 online submissions for Reordered Power of 2.
# Memory Usage: 14.2 MB, less than 76.21 % of Python3 online submissions for Reordered Power of 2.
from collections import Counter


class Solution:
    def convertToNum(self, stack):
        total = 0
        for num in stack:
            total *= 10
            total += num
        return total

    def traverse(self, counter, stack):
        if self.len == len(stack) and stack[0] != 0:
            num = self.convertToNum(stack)
            self.isPowerOfTwo = self.isPowerOfTwo or (
                num > 0 and (num & (num - 1)) == 0)
            return

        for key, val in counter.items():
            if val > 0 and not self.isPowerOfTwo:
                stack.append(key)
                counter[key] -= 1
                self.traverse(counter, stack)
                counter[key] += 1
                stack.pop()

    def reorderedPowerOf2(self, N: int) -> bool:
        counter = Counter()
        self.len = 0
        while N:
            tmp = N % 10
            N //= 10
            counter[tmp] += 1
            self.len += 1
        self.isPowerOfTwo = False
        self.traverse(counter, [])
        return self.isPowerOfTwo
