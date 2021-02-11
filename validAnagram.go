// problem: https://leetcode.com/problems/valid-anagram/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Valid Anagram.
// Memory Usage: 3 MB, less than 100.00% of Go online submissions for Valid Anagram.
package main

func isAnagram(s string, t string) bool {
	count := [26]int{}
	for _, character := range s {
		count[int(character)-97]++
	}
	for _, character := range t {
		count[int(character)-97]--
	}
	for _, character := range count {
		if character != 0 {
			return false
		}
	}
	return true
}
