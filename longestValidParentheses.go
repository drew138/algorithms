// problem: https://leetcode.com/problems/longest-valid-parentheses/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Longest Valid Parentheses.
// Memory Usage: 3.5 MB, less than 41.91% of Go online submissions for Longest Valid Parentheses.

package algorithmss

func maxNum(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func longestValidParentheses(s string) int {

	stack, max := []int{-1}, 0
	for i, char := range s {
		if char == '(' {
			stack = append(stack, i)
		} else if len(stack) == 1 {
			stack[0] = i
		} else {
			stack = stack[:len(stack)-1]
			max = maxNum(max, i-stack[len(stack)-1])
		}
	}
	return max
}
