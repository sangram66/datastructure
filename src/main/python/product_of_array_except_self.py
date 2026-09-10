
class Solution:
    def productExceptSelf(self, nums) :
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
        output = [1] * n
        i = 1
        print ("left_product")
        while i < n:
            left_product[i] = left_product[i-1] * nums[i-1]
            print (left_product)
            i += 1
        print ("right_product")
        i = n-1
        while i > 0:
            right_product[i-1] = right_product[i] * nums[i]
            print (right_product)
            i -= 1
        i = 0
        while i < n:
            output[i] = left_product[i] * right_product[i]
            i += 1
        return output
    
print (Solution().productExceptSelf([9,0,-2]))

        l = len(nums)
        ansl=[1]*l
        ansr=[1]*l
        ans=[1]*l
        for i in range(1,l):
            ansl[i]=ansl[i-1]*nums[i-1]
        
        for j in reversed(range(len(nums)-1)):
            ansr[j]=ansr[j+1]*nums[j+1]
        
        print (ansl)
        print (ansr)
        for i in range(0,l):
            ans[i]=ansl[i]*ansr[i]
            
        return ans