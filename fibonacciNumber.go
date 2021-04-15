// problem: https://leetcode.com/problems/fibonacci-number/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Fibonacci Number.
// Memory Usage: 1.9 MB, less than 100.00% of Go online submissions for Fibonacci Number.

package algorithms

func fib(n int) int {
	if n == 0 || n == 1 {
		return n
	}
	prev := 0
	cur := 1
	for i := 2; i <= n; i++ {
		prev, cur = cur, cur+prev
	}
	return cur
}
