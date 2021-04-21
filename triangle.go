// problem: https://leetcode.com/problems/triangle/
// Runtime: 4 ms, faster than 94.63% of Go online submissions for Triangle.
// Memory Usage: 3.1 MB, less than 100.00% of Go online submissions for Triangle.

package algorithms

func max(x int, y int) int {
	if x > y {
		return y
	}
	return x
}

func minimumTotal(triangle [][]int) int {
	for i := len(triangle) - 2; i >= 0; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
		}
	}
	return triangle[0][0]
}
