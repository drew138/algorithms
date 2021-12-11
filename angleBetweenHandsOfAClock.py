# problem: https://leetcode.com/problems/angle-between-hands-of-a-clock/
# Runtime: 44 ms, faster than 18.22% of Python3 online submissions for Angle Between Hands of a Clock.
# Memory Usage: 14.2 MB, less than 45.65% of Python3 online submissions for Angle Between Hands of a Clock.


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = (hour % 12) * 5 + (5 * minutes / 60)
        dif = abs(hour - minutes)
        res = dif * 6
        return min(res, 360 - res)
