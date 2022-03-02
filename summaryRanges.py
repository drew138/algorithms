# problem: https://leetcode.com/problems/summary-ranges/
# Runtime: 32 ms, faster than 84.38% of Python3 online submissions for Summary Ranges.
# Memory Usage: 13.9 MB, less than 61.40% of Python3 online submissions for Summary Ranges.

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sol = []
        if not nums: return nums
        start = nums[0]
        cur = nums[0]
        n = len(nums)
        for num in nums:
            if num - cur > 1:
                if start == cur:
                    sol.append(str(cur))                
                else:
                    sol.append(f"{start}->{cur}")
                start = num
            cur = num
        if start == cur:
            sol.append(str(cur))                
        else:
            sol.append(f"{start}->{cur}")
        return sol
