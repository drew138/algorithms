# problem: https://leetcode.com/problems/next-permutation/
# Runtime: 52 ms, faster than 14.29% of Python3 online submissions for Next Permutation.
# Memory Usage: 14.7 MB, less than 23.40% of Python3 online submissions for Next Permutation.


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from sortedcontainers import SortedList
        if len(nums) == 1:
            return
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        print(i)
        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        l = SortedList()
        k = len(nums) - 1
        while k > i:
            l.add(nums.pop())
            k -= 1
        while l:
            nums.append(l.pop(0))
