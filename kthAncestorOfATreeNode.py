# problem: https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
# Runtime: 1204 ms, faster than 87.32% of Python3 online submissions for Kth Ancestor of a Tree Node.
# Memory Usage: 112.1 MB, less than 11.71% of Python3 online submissions for Kth Ancestor of a Tree Node.

from collections import defaultdict
import math
from math import ceil

class TreeAncestor:

    def dfs(self, node, adj, up, cur_depth, depth, parent):
        depth[node] = cur_depth
        up[node][0] = parent[node]
        for j in range(1, self.log):
            self.up[node][j] = self.up[self.up[node][j - 1]][j - 1]
        
        for child in adj[node]:
            self.dfs(child, adj, up, cur_depth + 1, depth, parent)
        
    def create_adj(self, parent):
        adj = defaultdict(list)
        for i, val in enumerate(parent):
            adj[val].append(i)
        return adj
    
    def __init__(self, n: int, parent: List[int]):
        
        self.depth = [0] * n
        self.depth[0] = 0
        for i in range(1, n):
            self.depth[i] = self.depth[parent[i]] + 1
             
        self.log = int(ceil(math.log2(n)))
        self.up = [[0] * self.log for _ in range(n)]
        adj = self.create_adj(parent)
        self.dfs(0, adj, self.up, 0, self.depth, parent )

            
    def getKthAncestor(self, node: int, k: int) -> int:
        if self.depth[node] < k:
            return -1
        for i in range(self.log):
            if k & (1 << i):
                node = self.up[node][i]
        return node
# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)