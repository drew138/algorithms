package algorithms

// problem: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Number of Steps to Reduce a Number to Zero.
// Memory Usage: 1.9 MB, less than 15.12% of Go online submissions for Number of Steps to Reduce a Number to Zero.

func numberOfSteps(num int) int {
	ans := 0
	for num != 0 {
		ans++
		if num&1 == 1 {
			num -= 1
		} else {
			num >>= 1
		}
	}
	return ans
}
