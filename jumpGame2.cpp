// problem:https://leetcode.com/problems/jump-game-ii/
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Jump Game II.
// Memory Usage: 8.2 MB, less than 45.31% of C++ online submissions for Jump Game II.
#include <vector>

using namespace std;

class Solution
{
public:
    int jump(vector<int> &nums)
    {
        int m = nums[0];
        vector<int> dp(nums.size(), 2147483647);
        dp[0] = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            for (int j = 1; j <= nums[i]; ++j)
            {
                if (i + j >= dp.size())
                    break;
                dp[i + j] = min(dp[i] + 1, dp[i + j]);
            }
        }

        return dp[dp.size() - 1];
    }
    int jumpGreedy(vector<int> &nums)
    {
        if (nums.size() == 1)
            return 0;
        int cur = 0, answer = 0, tmp = 0;
        for (int i = 0; i < nums.size() - 1; ++i)
        {
            cur = max(cur, nums[i] + i);
            if (tmp == i)
            {
                ++answer;
                tmp = cur;
            }
        }
        return answer;
    }
};