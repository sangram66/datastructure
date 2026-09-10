'''
https://leetcode.com/problems/missing-number/
268. Missing Number
Easy
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
'''
class Solution(object):

    def missingNumber(self, nums):
        return int(((len(nums))*(len(nums)+1))/2 - sum(nums))
  
if __name__=="__main__":
    sol=Solution()
    nums=[9,6,4,2,3,5,7,0,1]
    print (sol.missingNumber(nums))
'''

def missing_number(num):
    nums=set(num)
    n=len(nums)+1   #since one number is missing so add 1
    for number in range(n):
        if number not in nums:
            return number
'''        
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)+1
        all_Sum=0
        num_sum=sum(nums)
        for i in range(missing):
            all_Sum+=i
        return (all_Sum-num_sum)        
'''
nums=[9,6,4,2,3,5,7,0,1]
print (missing_number(nums))