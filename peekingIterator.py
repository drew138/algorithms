# problem: https://leetcode.com/problems/peeking-iterator/submissions/
# Runtime: 32 ms, faster than 68.91% of Python3 online submissions for Peeking Iterator.
# Memory Usage: 14.6 MB, less than 36.45% of Python3 online submissions for Peeking Iterator.


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.hasN = iterator.hasNext()
        self.p = iterator.next() if self.hasN else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.p

    def next(self):
        """
        :rtype: int
        """
        tmp = self.p
        self.hasN = self.iterator.hasNext()
        self.p = self.iterator.next() if self.hasN else None
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.hasN


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
