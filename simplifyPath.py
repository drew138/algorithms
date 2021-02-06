# problem: https://leetcode.com/problems/simplify-path/
# Runtime: 32 ms, faster than 73.57% of Python3 online submissions for Simplify Path.
# Memory Usage: 14.4 MB, less than 49.65% of Python3 online submissions for Simplify Path.


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for p in path:
            if stack and p == "..":
                stack.pop()
            elif p == ".":
                continue
            elif not p in {" ", "", ".."}:
                stack.append(p)
        return "/" + "/".join(stack)
