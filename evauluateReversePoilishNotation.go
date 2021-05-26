// problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
// Runtime: 4 ms, faster than 91.67% of Go online submissions for Evaluate Reverse Polish Notation.
// Memory Usage: 4.2 MB, less than 65.74% of Go online submissions for Evaluate Reverse Polish Notation.

package algorithms

import (
	"strconv"
)

func evalRPN(tokens []string) int {
	stack := []int{}
	a, b := 0, 0
	for _, token := range tokens {
		// fmt.Println(stack)
		if token == "*" {
			a, stack = stack[len(stack)-1], stack[:len(stack)-1]
			b, stack = stack[len(stack)-1], stack[:len(stack)-1]
			stack = append(stack, a*b)
		} else if token == "+" {
			a, stack = stack[len(stack)-1], stack[:len(stack)-1]
			b, stack = stack[len(stack)-1], stack[:len(stack)-1]
			stack = append(stack, a+b)
		} else if token == "-" {
			a, stack = stack[len(stack)-1], stack[:len(stack)-1]
			b, stack = stack[len(stack)-1], stack[:len(stack)-1]
			stack = append(stack, b-a)
		} else if token == "/" {
			a, stack = stack[len(stack)-1], stack[:len(stack)-1]
			b, stack = stack[len(stack)-1], stack[:len(stack)-1]
			stack = append(stack, b/a)
		} else {
			number, _ := strconv.ParseInt(token, 10, 32)
			finalIntNum := int(number)
			stack = append(stack, int(finalIntNum))
		}
	}
	return stack[0]
}
