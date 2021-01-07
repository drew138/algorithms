# problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Runtime: 68 ms, faster than 52.48% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 75.40% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        chars = {}
        queue = deque()
        answer = 0
        for c in s:
            while queue and c in chars and chars[c]:
                char = queue.popleft()
                chars[char] = False
            queue.append(c)
            chars[c] = True
            answer = max(answer, len(queue))
        return answer
