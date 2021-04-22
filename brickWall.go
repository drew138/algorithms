// problem: https://leetcode.com/problems/brick-wall/
// Runtime: 64 ms, faster than 60.87% of Go online submissions for Brick Wall.
// Memory Usage: 7.5 MB, less than 65.22% of Go online submissions for Brick Wall.

package algorithmss

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func leastBricks(wall [][]int) int {
	num := 0
	quantities := map[int]int{}
	for _, row := range wall {
		for i := 0; i < len(row)-1; i++ {
			if i > 0 {
				row[i] += row[i-1]
			}
			quantities[row[i]] += 1
			num = max(quantities[row[i]], num)
		}
	}
	return len(wall) - num
}
