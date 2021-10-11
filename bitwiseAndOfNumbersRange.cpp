// problem: https://leetcode.com/problems/bitwise-and-of-numbers-range/
// Runtime: 4 ms, faster than 92.80% of C++ online submissions for Bitwise AND of Numbers Range.
// Memory Usage: 6 MB, less than 30.66% of C++ online submissions for Bitwise AND of Numbers Range.

class Solution
{
public:
	int rangeBitwiseAnd(int left, int right)
	{
		int shift = 0;
		while (left != right)
		{
			left >>= 1;
			right >>= 1;
			++shift;
		}
		return left << shift;
	}
};