// problem: https://leetcode.com/problems/add-digits/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Add Digits.
// Memory Usage: 2 MB, less than 100.00% of Go online submissions for Add Digits.

package algorithms

func addDigits(num int) int {
	for num >= 10 {
		cur := 0
		tmp := num
		for tmp > 0 {
			last := tmp % 10
			tmp /= 10
			cur += last
		}
		num = cur
	}
	return num
}
