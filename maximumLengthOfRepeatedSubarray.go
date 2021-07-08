// problem: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
// Runtime: 160 ms, faster than 28.74% of Go online submissions for Maximum Length of Repeated Subarray.
// Memory Usage: 20.6 MB, less than 12.64% of Go online submissions for Maximum Length of Repeated Subarray.

package algorithms

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func findLength(nums1 []int, nums2 []int) int {
	dp := [][]int{}

	answer := 0

	for i, num1 := range nums1 {
		dp = append(dp, []int{})
		for j, num2 := range nums2 {
			tmp := 0
			if num1 == num2 {
				tmp += 1
			}
			if i > 0 && j > 0 && tmp == 1 {
				tmp += dp[i-1][j-1]
			}
			dp[i] = append(dp[i], tmp)
			answer = max(answer, dp[i][j])
		}
	}
	return answer
}
