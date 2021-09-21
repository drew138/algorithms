// problem: https://leetcode.com/problems/max-consecutive-ones/
// Runtime: 32 ms, faster than 82.03% of C++ online submissions for Max Consecutive Ones.
// Memory Usage: 36.2 MB, less than 70.27% of C++ online submissions for Max Consecutive Ones.

#include <vector>

using namespace std;

class Solution
{
public:
	int findMaxConsecutiveOnes(vector<int> &nums)
	{
		int answer = 0;
		for (int i = 0; i < nums.size(); ++i)
		{
			int j = i;
			while (i < nums.size() && nums[i] == 1)
				++i;
			answer = max(answer, i - j);
		}
		return answer;
	}
};