// problem: https://leetcode.com/problems/average-of-levels-in-binary-tree/
// Runtime: 4 ms, faster than 97.44% of Go online submissions for Average of Levels in Binary Tree.
// Memory Usage: 6.2 MB, less than 87.18% of Go online submissions for Average of Levels in Binary Tree.

package algorithms

// TreeNode Definition for a binary tree.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfLevels(root *TreeNode) []float64 {
	queue := []*TreeNode{root}
	answer := []float64{}
	for len(queue) > 0 {
		tmp := []*TreeNode{}
		s := 0
		for _, node := range queue {
			s += node.Val
			if node.Left != nil {
				tmp = append(tmp, node.Left)
			}
			if node.Right != nil {
				tmp = append(tmp, node.Right)
			}
		}
		answer = append(answer, float64(s)/float64(len(queue)))
		queue = tmp
	}
	return answer
}
