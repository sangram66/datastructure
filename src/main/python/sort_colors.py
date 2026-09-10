class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0 # left pointer
        right =len(nums) -1 # right pointer
        index = 0 # current pointer, starting from the begining
        
        while index < len(nums):
            # if the current index indictating the large number but is in the smaller number's place 
            if nums[index] == 2 and index < right:
                nums[index], nums[right] = nums[right], nums[index]
                print("index < right:"+str(nums))
                right -= 1
            # if the current index indicating the small number but is in the bigger number's place
            elif nums[index] == 0 and index >left:
                nums[index], nums[left] =nums[left], nums[index]
                print("index >left"+str(nums))
                left  += 1
            # move the current index to next postion
            else:
                index += 1
                
        return nums
    
nums= [2,2,0,1,0,1]
print(Solution().sortColors(nums))