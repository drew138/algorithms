# problem: https://leetcode.com/problems/candy/
# Runtime: 152 ms, faster than 92.21% of Python3 online submissions for Candy.
# Memory Usage: 16.9 MB, less than 45.52% of Python3 online submissions for Candy.

from typing import List


class Solution:
    def getCandies(self, n):
        return n * (n + 1)//2

    def candy(self, ratings: List[int]) -> int:
        up = down = answer = prev = 0

        for i in range(1, len(ratings)):
            cur = 1 if ratings[i] > ratings[i-1] else - \
                1 if ratings[i] < ratings[i-1] else 0
            if (prev < 0 and cur >= 0) or (prev > 0 and cur == 0):
                answer += self.getCandies(up) + \
                    self.getCandies(down) + max(up, down)
                up = down = 0
            if cur > 0:
                up += 1
            elif cur < 0:
                down += 1
            else:
                answer += 1

            prev = cur
        answer += self.getCandies(up) + \
            self.getCandies(down) + max(up, down) + 1
        return answer
