// problem: https://leetcode.com/problems/ones-and-zeroes/
// Runtime: 32 ms, faster than 37.04% of Go online submissions for Ones and Zeroes.
// Memory Usage: 2.6 MB, less than 100.00% of Go online submissions for Ones and Zeroes.

package algorithms

import "strings"

func max(x uint8, y uint8) uint8 {
	if x > y {
		return x
	}
	return y
}

func findMaxForm(strs []string, m int, n int) int {
	dp := make([][]uint8, m+1)
	for i := range dp {
		dp[i] = make([]uint8, n+1)
	}
	for _, str := range strs {
		ones := strings.Count(str, "1")
		zeros := len(str) - ones
		for i := m; i >= zeros; i-- {
			for j := n; j >= ones; j-- {
				dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
			}
		}
	}
	return int(dp[m][n])
}
