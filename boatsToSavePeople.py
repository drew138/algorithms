# problem: https://leetcode.com/problems/boats-to-save-people/
# Runtime: 428 ms, faster than 99.06% of Python3 online submissions for Boats to Save People.
# Memory Usage: 21.1 MB, less than 49.58% of Python3 online submissions for Boats to Save People.

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        answer = 0
        while i <= j:
            if people[j] + people[i] <= limit:
                i += 1
            answer += 1
            j -= 1
        return answer
