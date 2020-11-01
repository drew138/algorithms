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

// question: https://leetcode.com/problems/rotate-image/submissions/
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Rotate Image.
// Memory Usage: 7.6 MB, less than 21.65% of C++ online submissions for Rotate Image.

class Solution
{
public:
    void rotate(vector<vector<int>> &matrix)
    {
        for (int i = 0; i < matrix.size(); ++i)
        {
            for (int j = i; j < matrix.size(); ++j)
            {
                int temp = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = temp;
            }
        }
        int max_i = matrix.size() - 1;
        for (int x = 0; x < matrix.size(); ++x)
        {
            for (int y = 0; y < (matrix.size() / 2); ++y)
            {
                int temp2 = matrix[x][y];
                matrix[x][y] = matrix[x][max_i - y];
                matrix[x][max_i - y] = temp2;
            }
        }
    }
};