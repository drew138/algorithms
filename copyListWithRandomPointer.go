// problem: https://leetcode.com/problems/copy-list-with-random-pointer/
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Copy List with Random Pointer.
// Memory Usage: 3.3 MB, less than 76.39% of Go online submissions for Copy List with Random Pointer.

package main

// Node for linked list
type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}
	cp := Node{head.Val, head.Next, head.Random}
	head.Next = &cp
	cur := cp.Next
	for cur != nil {
		cp := Node{cur.Val, cur.Next, cur.Random}
		cur.Next = &cp
		cur = cp.Next
	}
	mod := head.Next
	tmp := mod
	for tmp != nil {
		if tmp.Random != nil {
			tmp.Random = tmp.Random.Next
		}
		if tmp.Next != nil {
			tmp = tmp.Next.Next
		} else {
			tmp = nil
		}
	}
	tmp = mod
	for tmp != nil {
		if tmp.Next != nil {
			tmp.Next, head.Next = tmp.Next.Next, head.Next.Next
			head, tmp = head.Next, tmp.Next
		} else {
			tmp.Next = nil
			head.Next = nil
			break
		}
	}
	return mod
}
