// problem: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
// Runtime: 84 ms, faster than 47.22% of Go online submissions for Check If a String Contains All Binary Codes of Size K.
// Memory Usage: 10 MB, less than 11.11% of Go online submissions for Check If a String Contains All Binary Codes of Size K.

package algorithms

func hasAllCodes(s string, k int) bool {
	m := map[string]bool{}
	combs := 0
	for i := 0; i < len(s)-k+1; i++ {
		substr := s[i : i+k]
		if _, ok := m[substr]; ok {
			continue
		}
		m[substr] = true
		combs++
	}
	return combs == 1<<k
}
