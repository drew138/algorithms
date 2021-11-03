// problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Sum Root to Leaf Numbers.
// Memory Usage: 2.2 MB, less than 47.50% of Go online submissions for Sum Root to Leaf Numbers.
package algorithms

//   Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(root *TreeNode, cur int) int {
	if root == nil {
		return 0
	}
	cur *= 10
	cur += root.Val
	l := dfs(root.Left, cur)
	r := dfs(root.Right, cur)
	if l == 0 && r == 0 {
		return cur
	}
	return l + r
}

func sumNumbers(root *TreeNode) int {
	return dfs(root, 0)
}
