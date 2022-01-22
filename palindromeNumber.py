# problem: https://leetcode.com/problems/palindrome-number/
# Runtime: 72 ms, faster than 54.02% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.4 MB, less than 15.86% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = []
        if x < 0:
            return False
        while x:
            n = x % 10
            x //= 10
            nums.append(n)
        return nums == nums[::-1]