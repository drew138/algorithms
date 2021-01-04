# problem: https://leetcode.com/problems/beautiful-arrangement/
# Runtime: 1832 ms, faster than 20.53% of Python3 online submissions for Beautiful Arrangement.
# Memory Usage: 14.4 MB, less than 20.32% of Python3 online submissions for Beautiful Arrangement.

class Solution:
    def _getPermutations(self, counter, n):
        for key, val in counter.items():
            if val > 0 and ((n % key == 0) or (key % n == 0)):
                counter[key] -= 1
                self._getPermutations(counter, n + 1)
                counter[key] += 1
                if n == self.n:
                    self.answer += 1

    def countArrangement(self, n: int) -> int:
        from collections import Counter
        self.n = n
        self.answer = 0
        counter = Counter([n for n in range(1, n + 1)])
        print(counter)
        self._getPermutations(counter, 1)
        return self.answer
