# problem: https://leetcode.com/problems/minimum-jumps-to-reach-home/
# Runtime: 304 ms, faster than 19.75% of Python3 online submissions for Minimum Jumps to Reach Home.
# Memory Usage: 17.5 MB, less than 19.93% of Python3 online submissions for Minimum Jumps to Reach Home.


from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        from collections import deque
        forbidden = set(forbidden)
        visited = set()
        queue = deque([(0, "f")])
        answer = 0
        while queue:
            tmp = deque()
            while queue:
                c, d = queue.popleft()
                if c == x:
                    return answer
                forbidden.add(c)
                if not c + a in forbidden and (c + a < 10000) and not (c+a, "f") in visited:
                    tmp.append((c + a, "f"))
                    visited.add((c + a, "f"))
                if (d != "b") and (c - b > 0) and (not (c-b in forbidden)) and not (c - b, "b") in visited:
                    tmp.append((c - b, "b"))
                    visited.add((c - b, "b"))
            queue = tmp
            answer += 1
        print(answer)
        return -1

# // https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/973814/Python-BFS
