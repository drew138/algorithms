# problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Runtime: 76 ms, faster than 49.69% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
# Memory Usage: 15.3 MB, less than 75.16% of Python3 online submissions for Minimum Moves to Equal Array Elements II.

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        med = nums[len(nums) // 2] if len(nums) % 2 != 0 else (
            nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) // 2
        for num in nums:
            answer += abs(int(num - med))
        return answer
