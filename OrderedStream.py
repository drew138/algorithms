# problem:https://leetcode.com/problems/design-an-ordered-stream/submissions/
# Runtime: 316 ms, faster than 50.00% of Python3 online submissions for Design an Ordered Stream.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Design an Ordered Stream.

class OrderedStream:

    def __init__(self, n: int):
        self.strings = [None] * (n + 1)
        self.indexInsert = 1

    def insert(self, id: int, value: str) -> List[str]:

        self.strings[id] = value
        answer = []

        for string in self.strings[self.indexInsert:]:
            if string == None:
                break
            else:
                answer.append(string)
        if answer:
            self.indexInsert += len(answer)
        return answer

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
