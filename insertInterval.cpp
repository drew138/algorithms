// problem : https : //leetcode.com/problems/insert-interval/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
	vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
	{

		bool inserted = false;
		vector<vector<int>> answer;
		if (intervals.size() > 0 && newInterval[0] < intervals[0][0])
		{
			answer.push_back(newInterval);
			inserted = true;
		}
		for (int i = 0; i < intervals.size(); ++i)
		{
			int n = answer.size() - 1;
			if (!inserted && i + 1 < intervals.size() && intervals[i][0] <= newInterval[0] && newInterval[0] <= intervals[i + 1][0])
			{
				if (intervals[i][1] < newInterval[0])
				{
					answer.push_back(intervals[i]);
				}
				int minVal = intervals[i][1] >= newInterval[0] ? intervals[i][0] : newInterval[0];
				int maxVal = max(newInterval[1], intervals[i][1]);
				while (i + 1 < intervals.size() && newInterval[1] >= intervals[i + 1][0])
				{
					maxVal = max(newInterval[1], intervals[i + 1][1]);
					++i;
				}
				vector<int> tmp;
				tmp.push_back(minVal);
				tmp.push_back(maxVal);
				answer.push_back(tmp);
				inserted = true;
			}
			else if (answer.size() > 0 && answer[answer.size() - 1][1] >= intervals[i][0])
			{
				answer[answer.size() - 1][1] = max(answer[answer.size() - 1][1], intervals[i][1]);
			}
			else
			{
				if (!inserted && intervals[i][0] <= newInterval[0] && intervals[i][1] >= newInterval[1])
					inserted = true;
				answer.push_back(intervals[i]);
			}
		}
		if (!inserted)
		{
			if (answer.size() > 0 && newInterval[0] <= answer[answer.size() - 1][1])
			{
				answer[answer.size() - 1][1] = max(answer[answer.size() - 1][1], newInterval[1]);
			}
			else
			{
				answer.push_back(newInterval);
			}
		}
		return answer;
	}
};