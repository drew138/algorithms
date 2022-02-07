// problem: https://leetcode.com/problems/find-the-difference/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Find the Difference.
// Memory Usage: 2.1 MB, less than 100.00% of Go online submissions for Find the Difference.

package algorithms

func findTheDifference(s string, t string) byte {
	count := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		count[s[i]]++
	}
	for i := 0; i < len(t); i++ {
		character := t[i]
		if _, ok := count[character]; ok {
			count[character]--
			if count[character] < 0 {
				return character
			}
		} else {
			return character
		}

	}
	return '0'
}
