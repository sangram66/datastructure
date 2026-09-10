class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)
        def backtrack(cur,pos):
            print ("cur,pos  "+str(cur),str(pos))
            res.append(cur[:])
            print ("res.append(cur[:])  "+str(res))
            if pos==n:
                print ("inside if pos==n  "+str(res))
                return
            for i in range(pos,n):
                print ("i = "+str(i))
                cur.append(nums[i])
                print ("cur.append(nums[i])  "+str(cur))
                backtrack(cur,i+1)
                print ("return i = "+str(i))
                cur.pop()
                print ("cur pop i = "+str(cur))
            
        backtrack([],0)
        return res
    
print (Solution().subsets([1,2]))