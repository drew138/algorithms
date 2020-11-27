# problem: https://leetcode.com/problems/partition-equal-subset-sum/
# Runtime: 712 ms, faster than 72.67% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 14.6 MB, less than 59.04% of Python3 online submissions for Partition Equal Subset Sum.

from typing import List


class Solution:

    def traverse(self, i, target):
        if target == 0:
            self.hasSolution = True
        if not self.hasSolution and i < len(self.nums) and target not in self.targets:
            self.traverse(i+1, target - self.nums[i])
            self.traverse(i+1, target)
            self.targets.add(target)

    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        self.nums = nums
        if sumNums % 2 == 1:
            return False
        target = sumNums / 2
        self.targets = set()
        self.hasSolution = False
        self.traverse(0, target)
        return self.hasSolution
