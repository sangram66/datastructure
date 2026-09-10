'''
https://leetcode.com/explore/interview/card/facebook/55/dynamic-programming-3/3038/

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

Approach:
Same as Subarray sum equals K with modification. Basic idea is that, If you get the same remainder again, it means that you've encountered some sum which is a multiple of K.

Explanation with example

Example:
nums = [23,2,4], k = 6
Lets walk through the code with the example. 
(i=0) : sums = 23 => 23%6 => (sums = 5)
(i=1) : sums = 5+2=7 => 7%6 => (sums = 1)
(i=2) : sums = 1+4=5 => 5%6 => (sums = 5)
We have encountered the same sums(remainder) again which means we have the subarray of sums%k = 0.
But, there's another aspect to this problem. The subarray must have a minimum size of 2.
That is why we check if (i - d[sums])>1.
In the above example, this if loop is executed when (i=2) and (d[sums]=1).
In other words, the same remainder(sums=5) has been encountered twice and then we check for the respective difference in indices.

Counter example to understand this. Lets take nums = [23,6], k = 6
(i=0) : sums = 23 => 23%6 => (sums = 5)
(i=1) : sums = 5+6=11 => 11%6 => (sums = 5)
So, the same sums(remainder) has appeared again which means we've found the subarray but it is not a subarray of size 2 or more.
Because they've occurred next to each other, which means that, we have just one element in the subarray which contributes.
If you remove 23 from the nums array and keep 6 alone, it will still be a subarray whose sum%k is 0. But, we want a subarray of size 2 or more.
This is the reason why we calculate the index difference and then return True.

Also, if your k==0, you don't need to find the remainder. So, you just keep adding the sums and repeat the rest of the process.

'''
'''
class Solution(object):
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2:
            return False

        # 0: -1 is for edge case that current sum mod k == 0
        # for when the current running sum is cleanly divisible by k
        # e.g: nums = [4, 2], k = 3
        sums = {0: -1}  # 0
        cumulative_sum = 0
        for idx, num in enumerate(nums):
            cumulative_sum += num

            for prev_sum in sums:
                if (cumulative_sum-prev_sum) % k == 0 and idx-sums[prev_sum] >= 2:
                    return True

            # if current sum mod k not in dict, store it so as to ensure the further values stay
            if cumulative_sum not in sums:
                sums[cumulative_sum] = idx

        return False
 '''       

class Solution:
    def checkSubarraySum(self, nums, k) :
        if not nums:
            return False
        
        cache = {0:-1}
        rem=0
        
        for i in range(len(nums)):
            print (cache)
            try:
                rem = (rem+nums[i])%k
            except ZeroDivisionError:
                rem = rem+nums[i]
            print (rem)    
            if rem in cache:
                if i-cache[rem]>1:
                #if i-cache[rem]>1 and sum(nums[cache[rem]:i])%k==0:  extra condition just for cases like [5,0,0,0],3)
                    return True
            else:
                cache[rem] = i
            
        return False
    
#print (Solution().checkSubarraySum([23,2,6,4,7],6))
#print (Solution().checkSubarraySum([5,0,0,0],3))
print (Solution().checkSubarraySum([23,2,6,4,7],6))

