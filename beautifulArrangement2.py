# problem : https://leetcode.com/problems/beautiful-arrangement-ii/
# Runtime: 44 ms, faster than 86.21% of Python3 online submissions for Beautiful Arrangement II.
# Memory Usage: 15 MB, less than 82.76% of Python3 online submissions for Beautiful Arrangement II.

from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = [x for x in range(1, n - k + 1)]
        i = 1
        while k > 0:
            answer.append(answer[-1] + i * k)
            i *= -1
            k -= 1
        return answer
