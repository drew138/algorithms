// problem: https://leetcode.com/problems/rotate-image/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Rotate Image.
// Memory Usage: 2.2 MB, less than 16.76% of Go online submissions for Rotate Image.

package algorithms

func rotate(matrix [][]int) {
	n := len(matrix)
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n/2; j++ {
			matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
		}
	}
}
