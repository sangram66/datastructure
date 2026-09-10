class Solution:
    def fourSum(self,nums, target):
        # Write your code here.
        array=nums
        targetSum=target
        allpairs={}
        quadraplets=set()
        for i in range(1, len(array) - 1):
            for j in range(i + 1, len(array)):
                curr = array[i] + array[j]
                diff = targetSum - curr
                if diff in allpairs:
                    for pair in allpairs[diff]:
                        quadraplets.add(tuple(sorted([pair[0] ,pair[1] ,array[i],array[j]])))
            for k in range(0,i):
                curr = array[i] + array[k]
                if curr not in allpairs:
                    allpairs[curr] = [[array[k],array[i]]]
                else:
                    allpairs[curr].append([array[k],array[i]])
        return quadraplets
    
    
nums = [1,0,-1,0,-2,2]
target = 0
print  (Solution().fourSum(nums,target))

