// problem: https://leetcode.com/problems/decompress-run-length-encoded-list/
// Runtime: 4 ms, faster than 84.48% of Go online submissions for Decompress Run-Length Encoded List.
// Memory Usage: 5.9 MB, less than 68.97% of Go online submissions for Decompress Run-Length Encoded List.

func decompressRLElist(nums []int) []int {
	answer := []int{}
	for i := 0; i < len(nums); i += 2 {
		for j := 0; j < nums[i]; j++ {
			answer = append(answer, nums[i+1])
		}
	}
	return answer
}