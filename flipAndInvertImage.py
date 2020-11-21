# problem: https://leetcode.com/problems/flipping-an-image/submissions/
# Runtime: 52 ms, faster than 53.65% of Python3 online submissions for Flipping an Image.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Flipping an Image.

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if (len(A[0]) % 2) == 0:
            num_iters = (len(A[0]) // 2)
        else:
            num_iters = (len(A[0]) // 2) + 1
        len_list = len(A[0]) - 1
        for l in A:
            for i in range(num_iters):
                temp = int(not (l[i]))
                l[i] = int(not l[len_list - i])
                l[len_list - i] = temp
        return A
