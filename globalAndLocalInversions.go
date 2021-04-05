// problem: problem: https: // leetcode.com/problems/global- and -local-inversions/
// Runtime: 44 ms, faster than 84.62% of Go online submissions for Global and Local Inversions.
// Memory Usage: 6.4 MB, less than 76.92% of Go online submissions for Global and Local Inversions.

package algorithms

func isIdealPermutation(A []int) bool {
	for i, val := range A {
		tmp := val - i
		if tmp > 1 || tmp < -1 {
			return false
		}
	}
	return true
}
