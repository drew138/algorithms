// problem: https://leetcode.com/problems/remove-palindromic-subsequences/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Remove Palindromic Subsequences.
// Memory Usage: 1.9 MB, less than 84.62% of Go online submissions for Remove Palindromic Subsequences.

package algorithms

func removePalindromeSub(s string) int {
	if len(s) == 0 {
		return 0
	}
	for i, j := 0, len(s)-1; i < j; i++ {
		if s[i] != s[j] {
			return 2
		}
		j--
	}
	return 1
}
