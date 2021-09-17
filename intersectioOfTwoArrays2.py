# problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Runtime: 53 ms, faster than 43.72% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14.5 MB, less than 41.10% of Python3 online submissions for Intersection of Two Arrays II.


from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        answer = []
        counter = Counter(nums1)
        for num in nums2:
            if counter[num]:
                answer.append(num)
                counter[num] -= 1

        return answer
