'''
503. Next Greater Element II
Medium

3414

112

Add to List

Share
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
'''
class Solution:
    def nextGreaterElements(self, nums):
        ## RC ##
        ## APPROACH : STACK ##
        ## Similar to leetcode 739. Daily Temperatures ##
        
        ## LOGIC ##
        ## 1. Monotone decreasing stack to find NGE (next greater element)
        ## 2. In the first loop, we fill NGE all possible.
        ## 3. In the second loop, there might be some elements left in the stack, so we iterate again (without appending to stack) and get NGE
        ## 4. The elements that are left in the stack even after second loop are max(nums).
        
        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##

        stack, res = [], [-1] * len(nums)
        for i, num in enumerate(nums):              # 2
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(i)
            
        print (res)
        print (stack)
        for i, num in enumerate(nums):              # 3
            while stack and nums[stack[-1]] < num:
                print (num)
                res[stack.pop()] = num
        return res
    
print (Solution().nextGreaterElements([1,2,3,4,3]))
    
