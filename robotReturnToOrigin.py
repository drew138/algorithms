# problem: https://leetcode.com/problems/robot-return-to-origin/
# Runtime: 188 ms, faster than 5.50% of Python3 online submissions for Robot Return to Origin.
# Memory Usage: 14.3 MB, less than 84.56% of Python3 online submissions for Robot Return to Origin.


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m = {"H": 0, "V": 0}
        for c in moves:
            m["V"] += c == "U"
            m["V"] -= c == "D"
            m["H"] += c == "R"
            m["H"] -= c == "L"
        return m["H"] == 0 and m["V"] == 0
