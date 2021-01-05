# problem: https://leetcode.com/problems/best-team-with-no-conflicts/
# Runtime: 2228 ms, faster than 47.63% of Python3 online submissions for Best Team With No Conflicts.
# Memory Usage: 14.4 MB, less than 94.97% of Python3 online submissions for Best Team With No Conflicts.


from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(zip(ages, scores))
        players.sort()
        dp = [player[1] for player in players]
        for i in range(len(dp)):
            for j in range(i):
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        return max(dp)
