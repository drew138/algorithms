// problem: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
// Runtime: 152 ms, faster than 5.47% of C++ online submissions for Maximum Points You Can Obtain from Cards.
// Memory Usage: 42.4 MB, less than 45.06% of C++ online submissions for Maximum Points You Can Obtain from Cards.

#include <vector>
using namespace std;

class Solution
{
public:
    int maxScore(vector<int> &cardPoints, int k)
    {
        int total = 0, tmp = 0;
        for (int i = 0; i < cardPoints.size(); ++i)
        {
            total += cardPoints[i];
            if (i < cardPoints.size() - k)
                tmp += cardPoints[i];
        }
        int window = tmp;
        for (int i = 0, j = cardPoints.size() - k; j < cardPoints.size(); ++i, ++j)
        {
            tmp += cardPoints[j] - cardPoints[i];
            window = min(window, tmp);
        }
        return total - window;
    }
};