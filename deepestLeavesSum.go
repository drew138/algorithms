// https://leetcode.com/problems/deepest-leaves-sum/
// Runtime: 36 ms, faster than 11.83% of Go online submissions for Deepest Leaves Sum.
// Memory Usage: 7.5 MB, less than 13.98% of Go online submissions for Deepest Leaves Sum.

package algorithms

import "container/list"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func deepestLeavesSum(root *TreeNode) int {

	queue := list.New()
	queue.PushBack(root)
	answer := 0
	for queue.Len() > 0 {
		tmp := list.New()
		cur := 0
		for queue.Len() > 0 {
			e := queue.Front()
			element := queue.Remove(e).(*TreeNode)
			cur += element.Val
			if element.Left != nil {
				tmp.PushBack(element.Left)
			}
			if element.Right != nil {
				tmp.PushBack(element.Right)
			}
		}
		answer = cur
		queue = tmp
	}
	return answer
}
