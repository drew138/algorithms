// problem: https://leetcode.com/problems/guess-number-higher-or-lower/
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Guess Number Higher or Lower.
// Memory Usage: 5.7 MB, less than 99.59% of C++ online submissions for Guess Number Higher or Lower.

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 */
int guess(int num);

class Solution
{
public:
	int guessNumber(int n)
	{
		int left = 0, right = n, mid;
		while (left < right)
		{
			mid = (right - left) / 2 + left;
			if (guess(mid) > 0)
			{
				++mid;
				left = mid;
			}
			else
			{
				right = mid;
			}
		}
		return mid;
	}
};