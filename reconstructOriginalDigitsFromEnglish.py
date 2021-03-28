# problem: https://leetcode.com/problems/reconstruct-original-digits-from-english/
# Runtime: 52 ms, faster than 66.28% of Python3 online submissions for Reconstruct Original Digits from English.
# Memory Usage: 15.3 MB, less than 18.02% of Python3 online submissions for Reconstruct Original Digits from English.


class Solution:
    def originalDigits(self, s: str) -> str:
        from collections import Counter
        counter = Counter(s)
        answer = [0] * 10
        answer[0] = counter["z"]
        answer[2] = counter["w"]
        answer[4] = counter["u"]
        answer[6] = counter["x"]
        answer[8] = counter["g"]
        answer[1] = counter["o"] - answer[0] - answer[2] - answer[4]
        answer[3] = counter["h"] - answer[8]
        answer[5] = counter["f"] - answer[4]
        answer[7] = counter["s"] - answer[6]
        answer[9] = counter["i"] - answer[5] - answer[6] - answer[8]
        print(answer)
        characters = []
        for i, num in enumerate(answer):
            for _ in range(num):
                characters.append(str(i))
        return "".join(characters)
