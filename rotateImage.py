
# problem: https://leetcode.com/problems/rotate-image/
# Runtime: 36 ms, faster than 61.41% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.3 MB, less than 99.99% of Python3 online submissions for Rotate Image.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        size_matrix = len(matrix)
        half_size_matrix = (size_matrix-1)/2
        max_i = size_matrix - 1
        for i in range(size_matrix):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(size_matrix):
            for j in range(size_matrix/2):
                matrix[i][j], matrix[i][max_i -
                                        j] = matrix[i][max_i-j], matrix[i][j]
