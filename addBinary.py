# problem: https://leetcode.com/problems/add-binary/
# Runtime: 59 ms, faster than 9.18% of Python3 online submissions for Add Binary.
# Memory Usage: 14.2 MB, less than 55.41% of Python3 online submissions for Add Binary.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = []
        n = max(len(a), len(b))
        a = list(reversed(a))
        b = list(reversed(b))
        carry = "0"
        for i in range(n + 1):
            x = a[i] if i < len(a) else "0"
            y = b[i] if i < len(b) else "0"
            if i == n and carry == x == y == "0":
                break
            if x == y:
                l.append(carry)
                carry = x
            else:
                val = "0" if carry == "1" else "1"
                l.append(val)  
        return "".join(reversed(l))
                