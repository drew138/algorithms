# problem: https://leetcode.com/problems/reconstruct-itinerary/
# Runtime: 76 ms, faster than 81.82% of Python3 online submissions for Reconstruct Itinerary.
# Memory Usage: 14.6 MB, less than 86.82% of Python3 online submissions for Reconstruct Itinerary.
# sol: https://leetcode.com/problems/reconstruct-itinerary/discuss/989535/simple-python-solutions-(dfs-solution-and-iterative-solution-with-stack)

from typing import List


class Solution:
    def traverse(self, ap, m):
        while m[ap]:
            val = m[ap].pop()
            self.traverse(val, m)
        self.answer.append(ap)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        m = defaultdict(list)
        for ticket in sorted(tickets, reverse=True):
            m[ticket[0]].append(ticket[1])
        self.answer = []
        self.traverse("JFK", m)
        return self.answer[::-1]


sol = Solution()
sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"],
                   ["SFO", "SJC"], ["LHR", "SFO"]])
