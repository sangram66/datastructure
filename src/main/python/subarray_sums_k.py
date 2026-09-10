#https://leetcode.com/explore/interview/card/apple/344/array-and-strings/3115/
'''

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''

''''
from collections import defaultdict 
  
# Function to find number of subarrays   
# with sum exactly equal to k.  
def findSubarraySum(arr, n, Sum):  
   
    # Dictionary to store number of subarrays  
    # starting from index zero having   
    # particular value of sum.  
    prevSum = defaultdict(lambda : 0) 
    
    
    res = 0 
    
    # Sum of elements so far.  
    currsum = 0 
    
    for i in range(0, n):   
    
        # Add current element to sum so far.  
        currsum += arr[i] 
        print (arr[i]) 
        print (currsum)
    
        # If currsum is equal to desired sum,  
        # then a new subarray is found. So  
        # increase count of subarrays.  
        if currsum == Sum:   
            res += 1
            print ("res "+str(res))       
    
        # currsum exceeds given sum by currsum  - sum. 
        # Find number of subarrays having   
        # this sum and exclude those subarrays  
        # from currsum by increasing count by   
        # same amount.  
        if (currsum - Sum) in prevSum: 
            print ("inside if"+str(list(prevSum)))
            res += prevSum[currsum - Sum]  
            print ("inside if res "+str(res)) 
            
    
        # Add currsum value to count of   
        # different values of sum.  
        prevSum[currsum] += 1 
        print (list(prevSum))
       
    return res  
   
if __name__ == "__main__": 
  
    arr =  [10, 2, -2, -20, 10]   
    Sum = -10 
    n = len(arr)  
    print(findSubarraySum(arr, n, Sum))  
'''

def findSubarraySum(arr, n):  
    dicti={0:1}
    count=cumsum=0
    for num in arr:
        print ("num:"+str(num))
        cumsum+=num
        print ("cumsum:"+str(cumsum))
        print ("cumsum -n:"+str(cumsum-n))
        if cumsum-n in dicti:
            count+=dicti[cumsum-n]      #{0:1,2:1,3:2,4:1}    this is important as in dictionary we have increment the difference occurance
            print ("count:"+str(count))
        print (dicti)
        if cumsum in dicti:
            dicti[cumsum]+=1
        else:
            dicti[cumsum]=1
        print (dicti)
    return count
#arr=[0,0,0,0,0,0,0,0,0,0]
#k = 0
'''
arr =  [10, 2, -2, -20, 10,10,-10]   
k = -10 
arr=[1,1,1,1,1,1,1]
k = 2
'''
arr =  [1,1,1,1]
k = 2



print(findSubarraySum(arr,k))


        
        
    