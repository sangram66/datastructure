"""
class Solution:
    def productExceptSelf2(self, nums):
        aryRes = []
        for index in range(len(nums)):
            print ("index "+str(index))
            #print nums[:index], nums[index+1:]
            product_left = reduce(lambda x,y:x*y,nums[:index]) if(nums[:index]!=[]) else 1
            print ("product_left , nums[:index] "+str(product_left)+'       '+str(nums[:index]))
            product_right = reduce(lambda x,y:x*y,nums[index+1:]) if(nums[index+1:]!=[]) else 1
            print ("product_right , nums[index+1:] "+str(product_right)+'       '+str(nums[index+1:]))
            aryRes.append(product_left*product_right)
            print (aryRes)

        return aryRes
        
        
    

print Solution().productExceptSelf2([1,2,3,4])
"""
'''
class Solution:   
    def productExceptSelf3(self, nums):
        size = len(nums)
        ary_left = [1] * size
        ary_right = [1] * size
        ary_res = []

        for i in range(size-1):
            print ("left index , array left , nums[i]:"+str(i)+'   '+str(ary_left)+'  '+str(nums[i]))
            ary_left[i+1]*= ary_left[i]*nums[i]
            print ("array left"+str(ary_left))
        print ("------------------------")
        for i in range(size-1, 0, -1):
            print ("right index "+str(i))
            print ("right index , array right , nums[i]:"+str(i)+'   '+str(ary_right)+'  '+str(nums[i]))
            ary_right[i-1]*= ary_right[i]*nums[i]
            print ("array right , nums[i]: "+str(ary_right)+'  '+str(nums[i]))
    
        for i in range(size):
            ary_res.append(ary_left[i]*ary_right[i])
        return ary_res

print (Solution().productExceptSelf3([1,2,3,4]))
'''
class Solution:
    def productExceptSelf(self, nums):

        output = [1] * len(nums)
        print("output "+str(output))

        for i in range(1, len(nums)):
            output[i] = nums[i - 1] * output[i - 1]
        print("output "+str(output))
        r = 1

        for i in range(len(nums) - 1, -1, -1):
            print("i "+str(i))
            
            output[i] *= r
            print("output[i] "+str(output[i]))
            r *= nums[i]
            print("r "+str(r))

        return output
print (Solution().productExceptSelf([1,2,3,4]))


