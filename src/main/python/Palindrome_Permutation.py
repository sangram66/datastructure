'''
https://leetcode.com/problems/palindrome-permutation/
266. Palindrome Permutation
Easy
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
'''

from collections import defaultdict
class Solution(object):
    def canPermutePalindrome(self, s):   
        count = defaultdict(int)
        print (count)
        oddchar = 0
        for char in s:
            if count[char] == 1:
                count[char] -= 1
                print ("if count")
                print (count)
                oddchar -= 1
                print ("if oddchar" +str(oddchar))
            else:
                count[char] = 1
                print ("else count")
                print (count)
                oddchar +=1
                print ("else oddchar" +str(oddchar))
    
    
        if oddchar >1:
            return False
        return True
'''   
class Solution(object):
    def canPermutePalindrome(self, s):
        return len([count for count in collections.Counter(s).itervalues() if count % 2 == 1]) <= 1
'''
Input= "aab"
sol=Solution()
print (sol.canPermutePalindrome(Input))

