# problem: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/submissions/
# Runtime: 56 ms, faster than 24.23% of Python3 online submissions for Search in Rotated Sorted Array II.
# Memory Usage: 15 MB, less than 12.60% of Python3 online submissions for Search in Rotated Sorted Array II.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            if target == nums[l] or target == nums[r]:
                return True
            elif target < nums[r]:

                while l < r and nums[r - 1] == nums[r]:
                    r -= 1
                r -= 1
            elif target > nums[l]:

                while l < r and nums[l+1] == nums[l]:
                    l += 1
                l += 1
            else:
                break

        return False
