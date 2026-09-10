"""
907. Sum of Subarray Minimums
Medium

613

43

Favorite

Share
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
"""


class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = 10**9+7
        stack = [-1]
        print (stack[-1])
        A += [-float('inf')]
        print (A)
        res = 0
        print (list(enumerate(A)))
        for i,num in enumerate(A):
            while A[stack[-1]]>=num:
                print ("A[stack[-1]], num "+str(A[stack[-1]])+'     '+str(num)+'     '+str(stack[-1]))
                index = stack.pop()
                print ("index: "+str(index))
                if index == -1:return res%m
                left = index-stack[-1]
                right = i-index
                print ("left right"+str(left)+'     '+str(right))
                res += (left*right*A[index])%m
                print ("res "+str(res))
            stack.append(i)
        return (res)
    
print (Solution().sumSubarrayMins([3,1,2,4]))