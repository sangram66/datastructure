'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()

        for i in range(len(nums)-2):
            left = i + 1; right = len(nums) - 1
            target = 0 - nums[i]
            print(i,nums[i] , nums[i-1])
            if i == 0 or nums[i] != nums[i-1]:
                while left < right:
                    s = nums[left] + nums[right]
                    if s == target:
                        return s
                    elif s < target:
                        diff = s-target
                        left += 1
                    else:
                        right -= 1

        return results
nums=[-1,0,1,2,-1,-4]
print (Solution().threeSum(nums))
'''



class Solution:
    def threeSumClosest(self, nums, target) :
        nums.sort()
        sums = []
        print (nums)
        for i in range(len(nums) - 2):
            #if i > 0 and nums[i] == nums[i - 1]:
                #continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                print (nums[i] , nums[l] , nums[r])
                if current_sum == target:
                    return target
                else:
                    sums.append(current_sum)
                    print (sums)
                    if current_sum < target:
                        l += 1
                    else:
                        r -= 1
        closest_sum = [10001, 0]
        sums.sort()
        print (sums)
        for i in sums:
            diff = abs(target - i)
            if diff < closest_sum[0]:
                closest_sum[0], closest_sum[1] = diff, i
        return closest_sum[1]
    
#nums=[-1,0,1,2,-1,-4]
nums=[-1,2,1,-4]
print (Solution().threeSumClosest(nums,1))