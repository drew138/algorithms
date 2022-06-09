// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// Runtime: 25 ms, faster than 21.33% of Go online submissions for Two Sum II - Input Array Is Sorted.
// Memory Usage: 5.5 MB, less than 11.69% of Go online submissions for Two Sum II - Input Array Is Sorted.
package algorithms

func twoSum(numbers []int, target int) []int {
	i, j := 0, len(numbers)-1
	for true {
		if numbers[i]+numbers[j] == target {
			return []int{i + 1, j + 1}
		} else if numbers[i]+numbers[j] > target {
			j--
		} else if numbers[i]+numbers[j] < target {
			i++
		}

	}
	return []int{-1, -1}
}
