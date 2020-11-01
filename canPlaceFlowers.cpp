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

// problem: https://leetcode.com/problems/can-place-flowers/submissions/
// Runtime: 24 ms, faster than 99.56% of C++ online submissions for Can Place Flowers.
// Memory Usage: 20.7 MB, less than 56.12% of C++ online submissions for Can Place Flowers.

class Solution
{
public:
    bool canPlaceFlowers(vector<int> &flowerbed, int n)
    {
        int numFlowers = 0;

        bool canPlantPrev, canPlantNext, canPlantCurr;

        for (int i = 0; i < flowerbed.size(); ++i)
        {
            canPlantPrev = (i == 0) || !flowerbed[i - 1];
            canPlantNext = (i == (flowerbed.size() - 1)) || !flowerbed[i + 1];
            canPlantCurr = !flowerbed[i];
            if ((canPlantPrev && canPlantNext) && canPlantCurr)
            {
                numFlowers++;
                flowerbed[i] = 1;
            }
        }

        return (numFlowers >= n);
    }
};