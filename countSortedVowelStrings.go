// problem:https://leetcode.com/problems/count-sorted-vowel-strings/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Count Sorted Vowel Strings.
// Memory Usage: 1.9 MB, less than 100.00% of Go online submissions for Count Sorted Vowel Strings.

package algorithms

func combinations(n uint64, r uint64) int {
	divisor, dividend := uint64(1), uint64(1)
	for i := uint64(n - r + 1); i <= n; i++ {
		dividend *= i
	}
	for i := uint64(1); i <= r; i++ {
		divisor *= i
	}
	return int(dividend / divisor)
}

func countVowelStrings(n int) int {
	return combinations(uint64(n+4), uint64(4))
}
