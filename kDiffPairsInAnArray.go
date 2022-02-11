// problem: https://leetcode.com/problems/k-diff-pairs-in-an-array/
// Runtime: 8 ms, faster than 93.33% of Go online submissions for K-diff Pairs in an Array.
// Memory Usage: 6.1 MB, less than 57.78% of Go online submissions for K-diff Pairs in an Array.

package algorithms

func findPairs(nums []int, k int) int {
	counts := make(map[int]int)
	sol := 0
	for _, val := range nums {
		cur, exists := counts[val]
		if _, ok := counts[val+k]; ok && !exists {
			sol += 1
		}
		if _, ok := counts[val-k]; ok && !exists {
			sol += 1
		}
		if exists {
			if cur == 1 && k == 0 {
				sol += 1
			}
			counts[val]++
		} else {
			counts[val] = 1
		}
	}
	return sol
}
