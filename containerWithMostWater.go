// problem: https://leetcode.com/problems/container-with-most-water/
// Runtime: 16 ms, faster than 96.11% of Go online submissions for Container With Most Water.
// Memory Usage: 5.9 MB, less than 19.19% of Go online submissions for Container With Most Water.

package main

import "math"

func maxArea(height []int) int {
	i, j := 0, len(height)-1
	var answer float64 = 0
	var area float64
	for i < j {
		area = float64(j-i) * math.Min(float64(height[i]), float64(height[j]))
		answer = math.Max(answer, area)
		if height[i] < height[j] {
			i++
		} else {
			j--
		}
	}
	return int(answer)
}
