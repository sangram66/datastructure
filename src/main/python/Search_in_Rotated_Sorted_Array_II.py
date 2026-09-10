'''
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

'''

class Solution:
    def search(self, nums, target) :
        start, end = 0, len(nums)-1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if nums[mid] == target or nums[start] == target or nums[end] == target:
                return True
                
            elif nums[mid] < nums[end]: # right is sorted
                if nums[mid] < target and target < nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
            elif nums[mid] > nums[start]: # left is sorted
                if nums[start] < target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
                    
            else:
                end -= 1
                
s = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
t = 2 
print (Solution().search(s,t))