'''
416. Partition Equal Subset Sum
Share
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

'''
'''
def canPartition(nums):
    dp = {0}
    x=y={}
    for num in nums:
        print (num)
        print (dp)
        x={num - i for i in dp}
        y={num + i for i in dp} 
        print (x,y)
        dp = {num - i for i in dp} | {num + i for i in dp} 
    print (dp)
    return 0 in dp


nums = [1,5,11,5]
print (canPartition(nums))
'''

def canPartition(nums):
    
    if sum(nums)%k!=0:
        return False
    
    dp = set()
    
    dp.add(0) #if add empty subset it will lead to 0 i.e []
    target = sum(nums)//2
    
    
    for i in range(len(nums)):
       
        nextdp =set()
        for j in dp: #so we can't upadte the size of set during iteration or else it will throw error 
                                  #Set changed size during iteration

            if (j+nums[i])==target: 
                print (dp)
                return True     #incase only two equal subsets is required
            nextdp.add(j + nums[i])
            
            nextdp.add(j) # there is major reason we are the curr dp val here coz u see if just do nextdp.add(j + 

                          #nums[i]) then we will loose the 0 which will even let us loose the no itself which might
                          #be equal to target.
            
        
        dp = nextdp
    print (dp)  
    return True if target in dp else False
#nums = [1,5,11,5]
nums = [1,2,3,5]
k=2
print (canPartition(nums))
