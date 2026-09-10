'''

  Write a function that takes in an array of integers and returns a boolean
  representing whether the array is monotonic.

An array is monotonic if it is either monotone increasing or monotone decreasing.


sample input  = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
output=true

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
Example 4:

Input: nums = [1,2,4,5]
Output: true
Example 5:

Input: nums = [1,1,1]
Output: true
'''
'''
def monotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1,len(array)):
        if array[i] > array[i-1]:
            isNonIncreasing=False
        if array[i] < array[i-1]:
            isNonDecreasing=False
    
    return isNonIncreasing or isNonDecreasing


array=[-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print (monotonic(array))
            
'''

class Solution:
    def isMonotonic(self, A) :
        if A[-1] < A[0]: 
            A = A[::-1]
        print (A)

        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True
array=[-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print (Solution().isMonotonic(array))
'''

class Solution:
    def isMonotonic(self, nums) :
        return True if nums==sorted(nums) or nums==sorted(nums,reverse=True) else False
array=[-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print (Solution().isMonotonic(array))
'''


       