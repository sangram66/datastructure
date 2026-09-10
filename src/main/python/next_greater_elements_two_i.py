'''
496. Next Greater Element I
Easy

1039

79

Add to List

Share
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.

'''
def nextGreaterElement( nums1, nums2):
    if not nums1 or not nums2:
        return None 
    
    mapper = {}
    #create a dict for storing the nextgreater value for each element in the nums 1
    stack = [nums2[0]]
    #the stack is start with the first element in nums2 
    for i in range(1,len(nums2)):
        #iter each element in the nums2
        # if element greater than the previous element we pop them to the mapper
        #mapper={ element : greater element....} so that we can know that for each element we                
        #have their greater element and conencted as pair in mapper
        while stack and nums2[i]> stack[-1]:
            mapper[stack.pop()]= nums2[i]
        #if element smaller then the previous element we add it into stack 
        stack.append(nums2[i])
        
        
    print (mapper)
    print (stack)
    #after lopping the nums2, the element in the stack is the greatest element so we assign -1           
    #because we do not have any greater value  
    for key in stack:
        mapper[key]=-1
    print (mapper)
    #key in nums1 and get corresponding greater value in mapper
    return [mapper[key] for key in nums1]

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print (nextGreaterElement(nums1,nums2))