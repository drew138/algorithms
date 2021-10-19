# problem: https://leetcode.com/problems/next-greater-element-i/
# Runtime: 49 ms, faster than 61.52% of Python3 online submissions for Next Greater Element I.
# Memory Usage: 14.7 MB, less than 14.67% of Python3 online submissions for Next Greater Element I.


from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        m = {}
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            m[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])

        sol = [m[num] for num in nums1]

        return sol
