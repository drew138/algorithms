// problem: https://leetcode.com/problems/combination-sum-ii/
// Runtime: 4 ms, faster than 89.86% of C++ online submissions for Combination Sum II.
// Memory Usage: 10.7 MB, less than 51.13% of C++ online submissions for Combination Sum II.

#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
	void backtrack(vector<int> &candidates, vector<int> &current, vector<vector<int>> &answer, int target, int start)
	{
		if (target < 0)
			return;
		if (!target)
		{
			vector<int> copy = current;
			answer.push_back(copy);
		}
		for (int i = start; i < candidates.size(); ++i)
		{
			if (i > start && candidates[i] == candidates[i - 1])
				continue;
			current.push_back(candidates[i]);
			this->backtrack(candidates, current, answer, target - candidates[i], i + 1);
			current.pop_back();
		}
	}

	vector<vector<int>> combinationSum2(vector<int> &candidates, int target)
	{
		vector<vector<int>> answer;
		sort(candidates.begin(), candidates.end());
		vector<int> current;
		this->backtrack(candidates, current, answer, target, 0);
		return answer;
	}
};