// problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
// Runtime: 8 ms, faster than 88.19% of Go online submissions for Minimum Remove to Make Valid Parentheses.
// Memory Usage: 7.1 MB, less than 40.97% of Go online submissions for Minimum Remove to Make Valid Parentheses.

package algorithms

func minRemoveToMakeValid(s string) string {
	chars := []rune{}
	for _, c := range s {
		chars = append(chars, c)
	}
	stack := []int{}
	for i, c := range chars {
		if c == '(' {
			stack = append(stack, i)
		} else if len(stack) > 0 && c == ')' {
			stack = stack[:len(stack)-1]
		} else if c == ')' {
			chars[i] = '*'
		}
	}
	for _, j := range stack {
		chars[j] = '*'
	}
	answer := []rune{}
	for _, c := range chars {
		if c != '*' {
			answer = append(answer, c)
		}
	}
	return string(answer)
}
