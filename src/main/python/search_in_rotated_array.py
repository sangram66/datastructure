def search (arr, l, h, key):
    if l > h:
        return -1
     
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
 
    # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:
 
        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid-1, key)
        return search(arr, mid + 1, h, key)
 
    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid-1, key)
 
# Driver program
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
i = search(arr, 0, len(arr)-1, key)
if i != -1:
    print ("Index: % d"% i)
else:
    print ("Key not found")
    
    
'''

class Solution:
    def helper(self, nums, l, h, key):
        while l<=h:
            mid = (l+h)//2
            if nums[mid] == key:
                return mid
            if nums[mid] >= nums[l]:
                #left part is sorted perfectly
                #see whether our key lies in left side sorted range 
                if nums[l]<=key<nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
            else:
                #It is clear left part is clumsy and by observation it is clear that right part is sorted
                #see whether our key lies in right side sorted range 
                if nums[mid]<key<=nums[h]:
                    l = mid+1
                else:
                    h = mid-1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums,0, len(nums)-1, target)
        
    
'''
 