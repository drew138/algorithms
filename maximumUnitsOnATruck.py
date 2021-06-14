# problem: https://leetcode.com/problems/maximum-units-on-a-truck/
# Runtime: 152 ms, faster than 76.64% of Python3 online submissions for Maximum Units on a Truck.
# Memory Usage: 14.9 MB, less than 12.29% of Python3 online submissions for Maximum Units on a Truck.

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        answer = 0
        for box in boxTypes:
            if not truckSize:
                break
            tmp = min(box[0], truckSize)
            answer += tmp * box[1]
            truckSize -= tmp
        return answer
