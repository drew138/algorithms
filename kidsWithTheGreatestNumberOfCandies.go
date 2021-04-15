// problem: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Kids With the Greatest Number of Candies.
// Memory Usage: 2.3 MB, less than 7.67% of Go online submissions for Kids With the Greatest Number of Candies.

func kidsWithCandies(candies []int, extraCandies int) []bool {
	max := 0
	for _, val := range candies {
		if val > max {
			max = val
		}
	}
	answer := []bool{}
	for _, val := range candies {
		answer = append(answer, val+extraCandies >= max)
	}
	return answer
}