# problem: https://leetcode.com/problems/top-k-frequent-elements/
# Runtime: 170 ms, faster than 29.01% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 19.4 MB, less than 16.40% of Python3 online submissions for Top K Frequent Elements.


from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        counter = Counter(nums)
        for key, val in counter.items():
            buckets[val].append(key)
        return [val for bucket in buckets for val in bucket][::-1][:k]
        
