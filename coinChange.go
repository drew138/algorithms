// problem: https: // leetcode.com/problems/coin-change/
// Runtime: 4 ms, faster than 99.29% of Go online submissions for Coin Change.
// Memory Usage: 6 MB, less than 85.41% of Go online submissions for Coin Change.

package algorithms

import "math"

func min(a int, b int) int {
	if a <= b {
		return a
	}
	return b
}

func coinChange(coins []int, amount int) int {
	dp := make([]int, amount+1)
	dp[0] = 0
	for i := 1; i <= amount; i++ {
		dp[i] = math.MaxInt32
	}
	for i, _ := range dp {
		for j, _ := range coins {
			if i-coins[j] < 0 {
				continue
			}
			dp[i] = min(dp[i], dp[i-coins[j]]+1)
		}
	}
	if dp[amount] == math.MaxInt32 {
		return -1
	}
	return dp[amount]
}
