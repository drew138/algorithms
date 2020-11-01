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

//problem: https://leetcode.com/problems/longest-uncommon-subsequence-ii/
// Runtime: 4 ms, faster than 79.90% of C++ online submissions for Longest Uncommon Subsequence II.
// Memory Usage: 9 MB, less than 5.74% of C++ online submissions for Longest Uncommon Subsequence II.

class Solution
{
public:
    bool contains(string str1, string str2)
    {
        int strOneLength = str1.length();
        int strTwoLength = str2.length();
        int i = 0, j = 0;
        while (j < strTwoLength)
        {
            if (str1.at(i) == str2.at(j))
            {
                cout << str1.at(i) << str2.at(j) << " ";
                ++i;
            }
            if (i == strOneLength)
                return true;
            ++j;
        }
        return false;
    }

    int findLUSlength(vector<string> &strs)
    {
        int maxUncommon = -1;

        sort(strs.begin(), strs.end(), [](const string &first, const string &second) {
            return first.size() > second.size();
        });
        set<string> seen, duplicates;
        for (int i = 0; i < strs.size(); ++i)
        {
            if (seen.find(strs[i]) != seen.end())
            {
                duplicates.insert(strs[i]);
            }
            else
            {
                seen.insert(strs[i]);
            }
        }
        for (int i = 0; i < strs.size(); ++i)
        {
            if (duplicates.find(strs[i]) == duplicates.end())
            {
                if (i == 0)
                {
                    return strs[i].length();
                }
                bool isContained = false;
                for (int j = 0; j < i; ++j)
                {
                    if (contains(strs[i], strs[j]))
                    {
                        isContained = true;
                    }
                }
                if (!isContained)
                {
                    return strs[i].length();
                }
            }
        }
        return maxUncommon;
    }
};