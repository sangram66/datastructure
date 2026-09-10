'''
Time Complexity: O(n). 
Auxiliary Space: O(1).
'''

class Solution(object):
    def moveZeroes(self, nums):
        firstZero = None
        for i in range(len(nums)):
            print (" Inside first loop      "+str(i))
            print (nums)
            if nums[i] == 0:
                firstZero = i
                print (" Inside firstzero  nums,firstZero    "+str(nums[i])+'   ,   '+str(firstZero))
                break
        if firstZero is None:
            return
        pointer = firstZero + 1
        print (" pointer      "+str(pointer))
        while pointer < len(nums):
            print (" Inside while      "+str(pointer))
            print (nums)
            if nums[pointer] != 0:
                print (" nums[pointer]      "+str(nums[pointer]))
                print (" nums[firstZero], nums[pointer]      "+str(nums[firstZero])+'   ,   '+str(nums[pointer]) )
                nums[firstZero], nums[pointer] = nums[pointer], nums[firstZero]
                firstZero += 1
                print (" firstZero      "+str(firstZero))
            pointer +=1
            print (" pointer      "+str(pointer))
        return
    
if __name__=='__main__':
    sol=Solution()
    nums=[1,2,3,0,5,0,5,6,7]
    print (nums)
    sol.moveZeroes(nums)
    print (nums)