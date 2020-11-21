# problem: https://leetcode.com/problems/two-sum/submissions/
# Runtime: 48 ms, faster than 77.36% of Python3 online submissions for Two Sum.
# Memory Usage: 14.4 MB, less than 99.03% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        numbers[nums[0]] = 0
        for i in range(1, len(nums)):
            if (target - nums[i]) in numbers:
                return [numbers[target-nums[i]], i]
            numbers[nums[i]] = i
