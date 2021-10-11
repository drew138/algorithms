// problem: https://leetcode.com/problems/diameter-of-binary-tree/
// Runtime: 4 ms, faster than 90.55% of Go online submissions for Diameter of Binary Tree.
// Memory Usage: 4.5 MB, less than 87.01% of Go online submissions for Diameter of Binary Tree.

package algorithms

//   Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func traverse(root *TreeNode) (int, int) {
	if root == nil {
		return 0, 0
	}
	rl, rc := traverse(root.Right)
	ll, lc := traverse(root.Left)
	return 1 + max(rl, ll), max(1+rl+ll, max(rc, lc))
}

func diameterOfBinaryTree(root *TreeNode) int {
	_, answer := traverse(root)
	return answer - 1
}
