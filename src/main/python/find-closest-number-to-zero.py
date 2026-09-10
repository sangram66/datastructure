'''


https://leetcode.com/problems/find-closest-number-to-zero/description/

Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.



Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.


'''
from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int],tgt) -> int:
        neg = []
        pos = []

        # Splitting negative and positive numbers
        for num in nums:
            if num < tgt:
                neg.append(num)
            else:
                pos.append(num)

        # If no negative numbers, return the smallest positive number
        if not neg:
            return min(pos)

        # If no positive numbers, return the largest negative number
        elif not pos:
            return max(neg)

        # Otherwise, compare closest to zero
        else:
            a = max(neg)  # Largest negative number (closest to 0)
            b = min(pos)  # Smallest positive number (closest to 0)

            # Return the number with the minimum absolute value (prefer larger number in case of tie)
            return abs(a) if (abs(a) == abs(b)) else (b if abs(b) < abs(a) else a)

nums = [-4,-2,1,4,8]
tgt=7
print (Solution().findClosestNumber(nums,tgt))