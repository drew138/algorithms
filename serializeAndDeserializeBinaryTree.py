# problem: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Runtime: 116 ms, faster than 95.28% of Python3 online submissions for Serialize and Deserialize Binary Tree.
# Memory Usage: 20.3 MB, less than 64.73% of Python3 online submissions for Serialize and Deserialize Binary Tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def traverse(self, root, characters):
        if not root:
            return
        characters.append(str(root.val))
        if not root.left and not root.right: return
        characters.append('(')
        self.traverse(root.left, characters)
        characters.append(')')
        characters.append('(')
        self.traverse(root.right, characters)
        characters.append(')')

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        characters = []
        self.traverse(root, characters)
        return ''.join(characters)

    def parse_value(self, data, i):
        value = 0
        length = len(data)
        negative = False
        if data[i] == '-':
            negative = True
            i += 1
        while i < length and data[i].isnumeric():
            value *= 10
            value += int(data[i])
            i += 1
        if negative:
            value = -value
        return value, i

    
    def create_tree(self, data, i = 0):
        if i >= len(data):
            return None, i

        val, i = self.parse_value(data, i)

        if i >= len(data) or data[i] == ')':
            return TreeNode(val, None, None), i

        if i + 1 < len(data) and data[i + 1] == ')':
            left, i = None, i + 2
        else:
            left, i = self.create_tree(data, i + 1)
            i += 1

        if i + 1 < len(data) and data[i + 1] == ')':
            right, i = None, i + 2
        else:
            right, i = self.create_tree(data, i + 1)
            i += 1
        node = TreeNode(val, left, right)
        return node, i
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root, _ = self.create_tree(data, 0)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))