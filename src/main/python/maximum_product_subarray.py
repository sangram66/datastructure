'''
Maximum Product Subarray
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution(object):
    def maxProduct(self, nums):

        localMax = localMin = globalMax = nums[0]
        
        for i in range(1, len(nums)):
            # Finding max and min subarray product that includes nums[i] and
            # elements to the left of nums[i]. Why we consider min subarray too is,
            # since it is product there will be a case where min subarray is a -ve
            # product and upon encountering another -ve value, it might reach a max
            # value.
            a = max(localMax * nums[i], nums[i], localMin * nums[i])
            b = min(localMax * nums[i], nums[i], localMin * nums[i])
            # Updating globalMax
            localMax=a
            localMin=b
            globalMax = max(globalMax, localMax)
        
        return globalMax  
       
print (Solution().maxProduct([-4,-3,-2]))
        
    
            