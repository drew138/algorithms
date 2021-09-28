# problem: https://leetcode.com/problems/unique-email-addresses/
# Runtime: 68 ms, faster than 39.72% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 14.4 MB, less than 59.62% of Python3 online submissions for Unique Email Addresses.


from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        answer = 0
        seen = set()
        for email in emails:
            names = email.split("@")
            tmp = []
            for character in names[0]:
                if character == "+":
                    break
                elif character != ".":
                    tmp.append(character)
                last = character
            new_name = "".join(tmp) + "@" + names[1]
            if new_name not in seen:
                answer += 1
                seen.add(new_name)
        return answer
