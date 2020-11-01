#include <bits/stdc++.h>

#define D(x) cout << #x << " = " << x << endl;
#define ios ios_base::sync_with_stdio(0), cin.tie(0);
#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define all(v) v.begin(), v.end()
#define allgreater(v) v.begin(), v.end(), greater<int>()
#define formap(map) for (const auto &[key, value] : map)
#define ms(ar, val) memset(ar, val, sizeof ar)
typedef long long ll;
typedef long double ld;

using namespace std;

// problem: https://leetcode.com/problems/third-maximum-number/submissions/
// Runtime: 16 ms, faster than 50.54% of C++ online submissions for Third Maximum Number.
// Memory Usage: 9.9 MB, less than 33.00% of C++ online submissions for Third Maximum Number.

class Solution
{
public:
    int thirdMax(vector<int> &nums)
    {
        long max = -2147483649, secMax = -2147483650, thirdMax = -2147483651;
        set<int> seen;
        int uniques = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            if ((nums[i] > thirdMax) && (seen.find(nums[i]) == seen.end()))
            {
                uniques++;
                if (nums[i] > max)
                {
                    thirdMax = secMax;
                    secMax = max;
                    max = nums[i];
                }
                else if (nums[i] > secMax)
                {
                    thirdMax = secMax;
                    secMax = nums[i];
                }
                else
                {
                    thirdMax = nums[i];
                }
                seen.insert(nums[i]);
            }
        }
        if (uniques < 3)
        {
            return max;
        }
        else
        {
            return thirdMax;
        }
    }
};