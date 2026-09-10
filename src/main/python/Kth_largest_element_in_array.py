'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

'''

import random
def findKthLargest( nums, k) :    
    pivot = random.choice(nums)
    print ("pivot:  "+str(pivot))
    print ("nums:  "+str(nums))
    print ("k:  "+str(k))
    left = [x for x in nums if x > pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]
    
    print (left,mid,right)

    L = len(left)
    M = len(mid)
    # Here there is no need of finding the length of right array, as we know that, if our k is greater than (L+M), 
    # then the Kth Largest Element is definitely going to be in the right array.
    
    if k <= L:
        return findKthLargest(left,k)
    elif k > (L+M):
        return findKthLargest(right,k-(L+M))
    else:
        return mid[0]
    
print (findKthLargest([3,2,1,5,6,4],2))

'''

pivot:  2
nums:  [3, 2, 1, 5, 6, 4]
[3, 5, 6, 4] [2] [1]
pivot:  4
nums:  [3, 5, 6, 4]
[5, 6] [4] [3]
pivot:  6
nums:  [5, 6]
[] [6] [5]
pivot:  5
nums:  [5]
[] [5] []
5

'''