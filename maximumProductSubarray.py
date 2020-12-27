# problem: https://leetcode.com/problems/maximum-product-subarray/
# Runtime: 48 ms, faster than 93.44% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 15.1 MB, less than 15.41% of Python3 online submissions for Maximum Product Subarray.

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] * nums[i] if nums[i-1] != 0 else nums[i]
            reverse[i] = reverse[i-1] * \
                reverse[i] if reverse[i-1] != 0 else reverse[i]
        ans = max(reverse + nums)
        return ans
