// problem: https://leetcode.com/problems/majority-element/
// Runtime: 13 ms, faster than 92.51% of Go online submissions for Majority Element.
// Memory Usage: 6.3 MB, less than 48.46% of Go online submissions for Majority Element.

package algorithms

func majorityElement(nums []int) int {
	sol, count := 0, 0
	for _, num := range nums {
		if count == 0 {
			sol = num
		}
		if num == sol {
			count++
		} else {
			count--
		}
	}
	return sol
}
