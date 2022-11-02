# problem:https://leetcode.com/problems/minimum-genetic-mutation/
# Runtime: 42 ms, faster than 76.16% of Python3 online submissions for Minimum Genetic Mutation.
# Memory Usage: 13.9 MB, less than 86.96% of Python3 online submissions for Minimum Genetic Mutation.

import collections
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        seen = set([start])
        queue = collections.deque([(start, 0)])
        characters = ['A', 'C', 'G', 'T']
        word_bank = set(bank)
        while queue:
            element, steps = queue.popleft()
            n = len(element)
            for i in range(n):
                for character in characters:
                    mutation = element[:i] + character + element[i + 1:]
                    if mutation in word_bank and mutation not in seen:
                        if mutation == end:
                            return steps + 1
                        seen.add(mutation)
                        queue.append((mutation, steps + 1))
        return -1
