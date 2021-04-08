// problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Letter Combinations of a Phone Number.
// Memory Usage: 2 MB, less than 40.04% of Go online submissions for Letter Combinations of a Phone Number.

package algorithms

import (
	"strconv"
	"strings"
)

func join(stack *[]rune) string {
	var sb strings.Builder
	for i := len(*stack) - 1; i >= 0; i-- {
		sb.WriteRune((*stack)[i])
	}
	return sb.String()
}

func traverse(idx int, nums *[]int, chars *[]string, answer *[]string, stack *[]rune) {
	if idx == len(*nums) {
		*answer = append(*answer, join(stack))
		return
	}
	for _, val := range (*chars)[(*nums)[idx]] {
		*stack = append(*stack, val)
		traverse(idx+1, nums, chars, answer, stack)
		*stack = (*stack)[:len(*stack)-1]
	}
}

func letterCombinations(digits string) []string {
	chars := []string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
	nums := []int{}
	num, _ := strconv.Atoi(digits)
	for num != 0 {
		nums = append(nums, num%10)
		num /= 10
	}
	answer := []string{}
	if digits == "" {
		return answer
	}
	stack := []rune{}
	traverse(0, &nums, &chars, &answer, &stack)
	return answer
}
