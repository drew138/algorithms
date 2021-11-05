// problem: https://leetcode.com/problems/sum-of-left-leaves/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Sum of Left Leaves.
// Memory Usage: 2.7 MB, less than 98.21% of Go online submissions for Sum of Left Leaves.
package algorithms

//  Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) int {
	if root == nil {
		return 0
	}
	total := 0
	if root.Left != nil && root.Left.Right == nil && root.Left.Left == nil {
		total += root.Left.Val
	} else {
		total += sumOfLeftLeaves(root.Left)
	}
	total += sumOfLeftLeaves(root.Right)
	return total
}
