// problem: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
// Runtime: 4 ms, faster than 97.67% of Go online submissions for How Many Numbers Are Smaller Than the Current Number.
// Memory Usage: 3.2 MB, less than 28.79% of Go online submissions for How Many Numbers Are Smaller Than the Current Number.

func smallerNumbersThanCurrent(nums []int) []int {
	n := make([]int, 101, 101)
	for _, val := range nums {
		n[val] += 1
	}
	answer := []int{}
	for _, val := range nums {
		tmp := 0
		for j := 0; j < val; j++ {
			tmp += n[j]
		}
		answer = append(answer, tmp)
	}
	return answer
}