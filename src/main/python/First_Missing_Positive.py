#https://leetcode.com/explore/featured/card/google/59/array-and-strings/457/discuss/281436/python-beat-99.43
"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        for i in range(len(nums)):
            print (nums[i])
            if nums[i] < 0 and nums[i] > len(nums):
                nums[i]=0
                print (nums[i])
        nums.sort()
        print (nums)
        for i in range(1,len(nums)+2):
            print (len(nums))
            if i not in nums:
                return i
            
if __name__=="__main__":
    sol=Solution()
    nums=[3,4,-1,1]
    print (sol.firstMissingPositive(nums))
