''''
https://leetcode.com/problems/gray-code/
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
'''''

class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        print ("number to graycode: "+str(n))
        res = self.grayCode(n-1)
        print ("after graycode: "+str(n))
        
        num = 2**(n-1)
        print ("num: "+str(num))
        res += res[::-1]
        print ("res: "+str(res))
        for i in range(num,len(res)):
            print ("i: "+str(i))
            res[i] ^= num
            print (res)
        return (res)
    
print (Solution().grayCode(3))

"""
class Solution(object):
    def grayCode(self, n):
        if n==0:
            return [0]
        elif n==1:
            return [0,1]
        else:
            print ("step 0")
            print ("n= "+str(n))
            l1 = self.grayCode(n-1)
            print ("step 1")
            print (l1)
            l2 = [l+(1<<(n-1)) for l in l1[::-1]]
            return l1+l2
        return l1+l2
    
print (Solution().grayCode(5))
"""

