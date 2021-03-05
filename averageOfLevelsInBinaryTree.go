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
		s, l := 0, 0
		for _, node := range queue {
			s += node.Val
			l++
			if node.Left != nil {
				tmp = append(tmp, node.Left)
			}
			if node.Right != nil {
				tmp = append(tmp, node.Right)
			}
		}
		answer = append(answer, float64(s)/float64(l))
		queue = tmp
	}
	return answer
}
