// problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
// Runtime: 4 ms, faster than 72.61% of C++ online submissions for Search in Rotated Sorted Array.
// Memory Usage: 11 MB, less than 96.14% of C++ online submissions for Search in Rotated Sorted Array.

#include <vector>

using std::vector;

class Solution
{
public:
	int binarySearch(vector<int> &nums, int target, int left, int right)
	{
		int mid;
		while (left < right)
		{
			mid = (right - left) / 2 + left;
			if (nums[mid] == target)
			{
				return mid;
			}
			else if (nums[mid] < target)
			{
				left = mid + 1;
			}
			else
			{
				right = mid;
			}
		}
		return left == right && left < nums.size() && nums[left] == target ? left : -1;
	}

	int search(vector<int> &nums, int target)
	{
		int left = 0, right = nums.size(), mid;
		if (nums.size() == 1)
			return nums[0] == target ? 0 : -1;
		if (nums[left] > nums[right - 1])
		{
			while (left < right)
			{
				mid = (right - left) / 2 + left;
				if (nums[mid] < nums[mid - 1])
					break;
				else if (nums[mid] > nums[nums.size() - 1])
				{
					left = mid + 1;
				}
				else
				{
					right = mid;
				}
			}
			bool greater_than_target = nums[nums.size() - 1] >= target;
			left = greater_than_target ? mid : 0;
			right = greater_than_target ? nums.size() : mid - 1;
		}

		return this->binarySearch(nums, target, left, right);
	}
};