'''
https://leetcode.com/problems/valid-palindrome-ii/

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Understanding with example: s = "annma", rever = "amnna".
On comparing both of these strings, we evaluated in the second iteration that rever[i] (i.e. "m") != j (i.e. n). This gives us two options, either to remove "m" out of rever i.e. the reversed string of s or to remove "n" from s.
Tag 1:
We removed "m" from rever. If it is palindrome return True else move to Tag 2.
Tag 2:
Removing "n" from the string s. If palindrome, return True else return False.

'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        rever = s[::-1]
        if s == rever:
            return True
        else:
            for i, j in enumerate(s):
                
                if rever[i] != j:
                    print ("Tag 1")
                    rever = rever[0:i] + rever[i+1:]
                    print (rever)
                    if rever == rever[::-1]:
                        return True
                    print ("Tag 2")
                    s = s[0:i] + s[i+1:]
                    return s == s[::-1] 
                

Input= "amnna"
sol=Solution()
print (sol.validPalindrome(Input))
