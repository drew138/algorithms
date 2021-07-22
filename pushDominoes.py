# problem: https://leetcode.com/problems/push-dominoes/
# Runtime: 292 ms, faster than 19.16% of Python3 online submissions for Push Dominoes.
# Memory Usage: 16.4 MB, less than 75.33% of Python3 online submissions for Push Dominoes.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        answer = []
        a, b = "L", dominoes[0] if dominoes[0] in {"L", "R"} else "L"
        count = 0
        for domino in dominoes:
            if domino == ".":
                count += 1
                continue
            else:
                a = b
                b = domino
            if a == b:
                answer += [a for _ in range(count)]
            elif a == "L" and b == "R":
                answer += ["." for _ in range(count)]
            elif a == "R" and b == "L":
                answer += ["R" for _ in range(count//2)]
                if count % 2:
                    answer.append(".")
                answer += ["L" for _ in range(count//2)]
            count = 0
            answer.append(domino)
        if count and b == "L":
            answer += ["." for _ in range(count)]
        elif count and b == "R":
            answer += ["R" for _ in range(count)]
        return "".join(answer)
