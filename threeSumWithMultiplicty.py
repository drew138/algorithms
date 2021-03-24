# problem: https://leetcode.com/problems/3sum-with-multiplicity/
# Runtime: 100 ms, faster than 45.11% of Python3 online submissions for 3Sum With Multiplicity.
# Memory Usage: 14.4 MB, less than 53.76% of Python3 online submissions for 3Sum With Multiplicity.

from typing import List


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        from collections import Counter
        counter = Counter(A)
        mod = 10 ** 9 + 7
        answer = 0
        for i in range(101):
            for j in range(i+1, 101):
                k = target - i - j
                if j < k <= 100:
                    answer += counter[i] * counter[j] * counter[k]
                    answer %= mod
        for i in range(101):
            j = target - 2 * i
            if i < j <= 100:
                answer += counter[i] * (counter[i] - 1) / 2 * counter[j]
                answer %= mod
        for i in range(101):
            if (target - i) % 2 == 0:
                j = (target - i) / 2
                if i < j <= 100:
                    answer += counter[i] * counter[j] * (counter[j]-1)/2
                    answer %= mod
        if target % 3 == 0:
            i = target / 3
            if 0 <= i <= 100:
                answer += counter[i] * (counter[i] - 1) * (counter[i] - 2) / 6
                answer %= mod
        return int(answer)
