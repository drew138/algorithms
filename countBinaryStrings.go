// problem: https://leetcode.com/problems/count-binary-substrings/
// Runtime: 8 ms, faster than 87.80% of Go online submissions for Count Binary Substrings.
// Memory Usage: 5.9 MB, less than 36.59% of Go online submissions for Count Binary Substrings.

package algorithms

func min(x int, y int) int {
	if x < y {
		return x
	}
	return y
}

func countBinarySubstrings(s string) int {
	prev := 0
	cur := 0
	total := 0
	for i := range s {
		if i > 0 && s[i] != s[i-1] {
			prev = cur
			cur = 0
		}
		cur += 1
		if cur == min(cur, prev) {
			total++
		}
	}
	return total
}
