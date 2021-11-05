// problem: https://leetcode.com/problems/arranging-coins/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Arranging Coins.
// Memory Usage: 2.2 MB, less than 43.28% of Go online submissions for Arranging Coins.

package algorithms

import "math"

func arrangeCoins(n int) int {
	var tmp float64 = -0.5 + math.Sqrt(0.25+2.0*float64(n))
	return int(math.Floor(tmp))

}
