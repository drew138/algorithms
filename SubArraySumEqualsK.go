
// problem: https://leetcode.com/problems/subarray-sum-equals-k/
// Runtime: 60 ms, faster than 68.82% of Go online submissions for Subarray Sum Equals K.
// Memory Usage: 8.1 MB, less than 45.73% of Go online submissions for Subarray Sum Equals K.

package algorithms

func subarraySum(nums []int, k int) int {
    sol := 0
    m := make(map[int]int)
    m[0] = 1
    cur := 0
    for _, num := range nums {
        cur += num
        if val, ok := m[cur - k]; ok {
            sol += val
        }
        if _, ok := m[cur]; ok {
            m[cur]++
        } else {
            m[cur] = 1
        }
    }
    return sol
}

