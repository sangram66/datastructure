#https://leetcode.com/explore/featured/card/google/59/array-and-strings/464/
'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        while cnt < len(nums)-1:
            if nums[cnt] == nums[cnt+1]:
                nums.pop(cnt)
                print (nums)
                cnt+=1
            else:
                cnt+=1
        return cnt

if __name__=='__main__':   
    sol=Solution()
    print (sol.removeDuplicates([1,1,2]))
'''
from typing import List
class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1  # Pointer for the position of the next unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Check if the current element is different from the previous one
                nums[k] = nums[i]  # Place it in the next unique position
                print (nums)
                print (i)
                k += 1  # Move the pointer forward

        return k  # Return the number of unique elements

if __name__=='__main__':
    sol=Solution()
    #print (sol.removeDuplicates([1,1,2]))
    print (sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
                

'''

Time Complexity:
The algorithm traverses the list once using a single loop (for i in range(1, len(nums))), making the time complexity:
O(n)
where n is the length of nums.
Each element is processed once, and there are no nested loops, so the time complexity remains linear.

Space Complexity:
The algorithm modifies the array in-place, meaning it does not use extra space apart from a few integer variables (k and i).
Since it does not use any additional data structures (arrays, lists, etc.), the space complexity is:

O(1)
(constant space).
'''
            