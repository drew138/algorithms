# problem: https://leetcode.com/problems/queue-reconstruction-by-height/
# Runtime: 140 ms, faster than 62.75% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.7 MB, less than 6.40% of Python3 online submissions for Queue Reconstruction by Height.


from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for h, k in people:
            ans.insert(k, [h, k])
        return ans