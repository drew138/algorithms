# problem: https://leetcode.com/problems/permutations-ii/submissions/
# Runtime: 4196 ms, faster than 5.14% of Python3 online submissions for Permutations II.
# Memory Usage: 14.3 MB, less than 35.53% of Python3 online submissions for Permutations II.

class Solution:
    def getPermutation(self, node, visited, traversal, lenList):
        if lenList == len(traversal):
            self.permutations.add(tuple(traversal))
            return
        for index, element in enumerate(self.adj[node]):
            if element in visited:
                vis = visited.copy()
                vis.remove(element)
                trav = traversal.copy()
                trav.append(element)
                self.getPermutation(element,
                                    vis,
                                    trav,
                                    lenList)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.permutations = set()
        self.adj = {}
        for i in range(len(nums)):
            numsCopy = nums.copy()
            numsCopy.pop(i)
            self.adj[nums[i]] = numsCopy
        for num in nums:
            vis = nums.copy()
            vis.remove(num)
            self.getPermutation(num, vis, [num], len(nums))
        self.answer = [list(element) for element in self.permutations]
        return self.answer
