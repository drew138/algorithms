// problem: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
// Runtime: 161 ms, faster than 55.77% of Go online submissions for Minimum Domino Rotations For Equal Row.
// Memory Usage: 7.6 MB, less than 50.00% of Go online submissions for Minimum Domino Rotations For Equal Row.
package algorithms

func minValue(one, two int) int {
	if one < two {
		return one
	}
	return two
}

func minDominoRotations(tops []int, bottoms []int) int {
	top, bottom, repeated := [7]int{}, [7]int{}, [7]int{}
	n := len(tops)
	for i := 0; i < n; i++ {
		if tops[i] == bottoms[i] {
			repeated[tops[i]]++
		} else {
			top[tops[i]]++
			bottom[bottoms[i]]++
		}
	}

	for i := 0; i < 7; i++ {
		if (n - repeated[i] - top[i]) == bottom[i] {
			return minValue(top[i], bottom[i])
		}
	}

	return -1

}
