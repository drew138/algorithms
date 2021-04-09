// problem: https://leetcode.com/problems/verifying-an-alien-dictionary/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Verifying an Alien Dictionary.
// Memory Usage: 2.6 MB, less than 100.00% of Go online submissions for Verifying an Alien Dictionary.

package algorithms

import "strings"

func isAlienSorted(words []string, order string) bool {

	for i := 0; i+1 < len(words); i++ {
		for j, char := range words[i] {
			if j < len(words[i+1]) && strings.Index(order, string(char)) < strings.Index(order, string(words[i+1][j])) {
				break
			} else if j == len(words[i+1]) || strings.Index(order, string(char)) > strings.Index(order, string(words[i+1][j])) {
				return false
			}
		}
	}
	return true
}
