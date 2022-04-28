# problem: https://leetcode.com/problems/remove-element/
# Runtime: 71 ms, faster than 6.08% of Python3 online submissions for Remove Element.
# Memory Usage: 13.8 MB, less than 65.41% of Python3 online submissions for Remove Element.


from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        j = n - 1
        while j >= 0 and nums[j] == val:
            j -= 1
        if j < 0: return 0
        i = 0
        
        while i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                while nums[j] == val:
                    j -= 1
            i += 1
        for x in range(n):
            if nums[x] == val:
                return x 
        return n
