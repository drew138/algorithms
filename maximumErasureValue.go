package algorithms

// problem: https://leetcode.com/problems/maximum-erasure-value/submissions/
// Runtime: 189 ms, faster than 92.00% of Go online submissions for Maximum Erasure Value.
// Memory Usage: 10.2 MB, less than 20.00% of Go online submissions for Maximum Erasure Value.

func maximumUniqueSubarray(nums []int) int {
	seen := make([]bool, 10e5+1)
	i, j := 0, 0
	n := len(nums)
	answer := 0
	cur := 0
	for i < n && j < n {
		if !seen[nums[j]] {
			cur += nums[j]
			seen[nums[j]] = true
			j++
			if cur > answer {
				answer = cur
			}
		} else {
			cur -= nums[i]
			seen[nums[i]] = false
			i++
		}
	}
	return answer
}
