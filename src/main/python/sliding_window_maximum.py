'''
239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]

Approach
create a deque and an ans list to store the final ans
loop the the given input list
pop the deque from the right untill the rightmost element of the queue is greater than the current element in the loop (note that the deque is only storing the index)
insert the current elements index to the right of the deque
if the the leftmost element of the deque is equal to i-k then it is no longer under consideration so we pop it
for every cycle of the loop after the threshold i >=k-1 we push it to the ans list
'''
import collections
class Solution:
    def maxSlidingWindow(self, nums, k) :
        ans = []
        dq = collections.deque()  #step 1
        
        for i ,num in enumerate(nums):  #step2
            
            while dq and num > nums[dq[-1]]: #step3
                print (dq)
                dq.pop()
                
            dq.append(i) #step4
            
            if i-k == dq[0]: #step5
                print ('step 5'+str(dq))
                dq.popleft()
                
            if i >= k-1: #step6
                ans.append(nums[dq[0]])
                
            
        return ans  
    
nums = [1,3,-1,-3,5,3,6,7] 
k = 3    
print (Solution().maxSlidingWindow(nums,k))
    
