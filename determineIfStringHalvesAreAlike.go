// problem: https://leetcode.com/problems/determine-if-string-halves-are-alike/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Determine if String Halves Are Alike.
// Memory Usage: 2.2 MB, less than 100.00% of Go online submissions for Determine if String Halves Are Alike.

package algorithms

import "strings"

func halvesAreAlike(s string) bool {
	vowels := "aeiouAEIOU"

	count := 0
	for _, val := range s[len(s)/2:] {
		if strings.ContainsAny(vowels, string(val)) {
			count++
		}
	}
	for _, val := range s[:len(s)/2] {
		if strings.ContainsAny(vowels, string(val)) {
			count--
		}
	}

	return count == 0
}
