'''

  Write a function that takes in a sorted array of integers as well as a target
  integer. The function should use the Binary Search algorithm to determine if
  the target integer is contained in the array and should return its index if it
  is, otherwise -1

 array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
 target = 33


'''
def binarySearch(array,target):
    return binarySearchHelper(array,target,0,len(array)-1)

def binarySearchHelper(array,target,left,right):
    if left > right:
        return -1
    
    middle = (left + right)//2
    match = array[middle]
    
    if target == match:
        return middle
    elif target < match:
        return binarySearchHelper(array,target,left,middle-1)
    else:
        return binarySearchHelper(array,target,middle+1,right)
    

print (binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))

'''
iterative 

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left <= right:
            mid=(left+right)/2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            if nums[mid]>target:
                right=mid-1
        return -1

'''