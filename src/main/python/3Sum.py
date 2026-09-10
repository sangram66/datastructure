'''
https://www.algoexpert.io/questions/Three%20Number%20Sum

  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.

array  = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0


'''
'''
def threeNumberSum(array, targetSum):
    # Write your code here.
    if len(set(array))==1 and list(set(array))[0]==targetSum:
        return array
    array.sort()
    print(array)
    triplets=[]
    for curr in range(len(array) -2):
        if array[curr-1] == array[curr]:
            curr = curr+1
        left = curr+1
        right =len(array)-1
        while left < right :
            if (array[curr] + array [left] + array[right] == targetSum)  :
                triplets.append([array[curr] , array [left] , array[right]])
                left += 1
                right -= 1
                
            elif array[curr] + array [left] + array[right] < targetSum:
                left += 1
            elif array[curr] + array [left] + array[right] > targetSum:
                right -= 1
                
    return (triplets)
#array=[12,3,1,2,-6,5,-8,6]
array=[0,0,0]
#array=[-1,0,1,2,-1,-4]
targetSum=0
print (threeNumberSum(array, targetSum))
'''

'''
##No duplicate resulst
class Solution:
    def threeSum(self, nums,tgt):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        print (nums)

        for i in range(len(nums)-2):
            left = i + 1; right = len(nums) - 1
            target = tgt - nums[i]
            print(i,nums[i] , nums[i-1])
            if i==0 or nums[i] != nums[i-1]:
                while left < right:
                    s = nums[left] + nums[right]
                    if s == target:
                        results.append([nums[i], nums[left], nums[right]])
                        print(results)
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1; right -=1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return results
#nums = [0,0,0]
nums=[-1,0,1,2,-1,-4]
print (Solution().threeSum(nums,0))
'''

#without sorting
class Solution:
    def threeSum(self, nums) :
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    print (-val1 - val2,complement,seen)
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                        print ("res :"+ str(res))
                    seen[val2] = i
                    print ("seen: "+str(seen))
        return res
    
nums=[-1,0,1,2,-1,-4]
#nums=[-9,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,-7,-5,9,11,-1,1,3,-15,-5,11,-12,-4,-4,-2,-6,-10,-6,-6,0,2,-9,14,-14,-14,-9,-1,-2,-7,-12,-13,-15,-4,-3,1,14,3,-12,3,3,-10,-9,-1,-7,3,12,-6,0,13,4,-15,0,2,6,1,3,13,8,-13,13,11,11,13,14,-6]
print (Solution().threeSum(nums))

#{(-1, -1, 2), (-8, 0, 8), (-2, 0, 2), (-2, 1, 1), (-1, 0, 1), (0, 0, 0)}
'''

class Solution:
    def threeSum(self, nums,target) :
        dup=set()
        res=set()
        seen={}
        for i,val1 in enumerate(nums):
            if val1 not in dup:
                dup.add(val1)
                for j,val2 in enumerate(nums[i+1:]):
                    comp=target-val1-val2
                    if comp in seen and seen[comp]==i:
                        res.add(tuple(sorted((val1,val2,comp))))
                        
                    seen[val2]=i
        return (res)
nums=[-1,0,1,2,-1,-4]  
print (Solution().threeSum(nums,0))  
'''
    