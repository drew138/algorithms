// problem: https://leetcode.com/problems/number-of-good-pairs/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Number of Good Pairs.
// Memory Usage: 2 MB, less than 22.06% of Go online submissions for Number of Good Pairs.

package algorithms

func combinations(n uint64, r uint64) int {
	divisor, dividend := uint64(1), uint64(1)
	for i := uint64(n - r + 1); i <= n; i++ {
		dividend *= i
	}
	for i := uint64(1); i <= r; i++ {
		divisor *= i
	}
	return int(dividend / divisor)
}

func numIdenticalPairs(nums []int) int {
	count := map[int]int{}
	answer := 0
	for _, num := range nums {
		_, ok := count[num]
		if ok {
			count[num]++
		} else {
			count[num] = 1
		}
	}
	for _, c := range count {
		if c > 1 {
			answer += combinations(uint64(c), uint64(2))
		}
	}
	return answer
}
