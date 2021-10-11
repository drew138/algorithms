// problem: https://leetcode.com/problems/3sum/
// Runtime: 84 ms, faster than 69.46% of C++ online submissions for 3Sum.
// Memory Usage: 21.2 MB, less than 47.86% of C++ online submissions for 3Sum.

#include <vector>
#include <algorithm>

using std::vector;

class Solution
{
public:
	vector<vector<int>> threeSum(vector<int> &nums)
	{
		vector<vector<int>> answer;
		if (nums.size() < 3)
			return answer;
		sort(nums.begin(), nums.end());
		for (int i = 0; i < nums.size(); ++i)
		{
			if (i != 0 && nums[i] == nums[i - 1])
				continue;
			int left = i + 1, right = nums.size() - 1;
			int cur = nums[i];
			while (left < right)
			{
				int sum = nums[left] + nums[right] + cur;
				if (sum < 0)
				{
					++left;
				}
				else if (sum == 0)
				{
					vector<int> tmp{nums[left], nums[right], cur};
					answer.push_back(tmp);
					++left;
					while (left < right && nums[left] == nums[left - 1])
					{
						++left;
					}
				}
				else
				{
					--right;
				}
			}
		}
		return answer;
	}
};