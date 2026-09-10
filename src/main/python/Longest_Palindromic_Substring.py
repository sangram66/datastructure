'''
Longest Palindromic Substring
Write a function that, given a string, returns its longest palindromic substring. A palindrome is defined as a string that is written the same forward and backward. Assume that there will only be one longest palindromic substring.
Sample input: "abaxyzzyxf" Sample output: "xyzzyx"
'''
'''
class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            print ("i: "+str(i))
            tmp = self.helper(s, i, i)
            print ("tmp in odd: "+str(tmp))
            if len(tmp) > len(res):
                res = tmp
                print ("res in odd:  "+str(tmp))
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            print ("tmp in even: "+str(tmp))
            if len(tmp) > len(res):
                res = tmp
                print ("res in even:  "+str(tmp))
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            print ("inside helper -> 1 ,l,r,return s[l+1:r]   "+str(l)+'   '+str(r)+'   '+str(s[l+1:r]))
            l -= 1; r += 1
            print ("inside helper,l,r,return s[l+1:r]   "+str(l)+'   '+str(r)+'   '+str(s[l+1:r]))
        return s[l+1:r]

#print (Solution().longestPalindrome("babad"))
print (Solution().longestPalindrome("abaxyzzyxf"))
'''

# O(n^2) time | O(1) space

def getlongestpalindromesubstring(string):
    currentLongest=[0,1]
    for i in range(1,len(string)):
        odd=getlongestpalindrome(string,i-1,i+1)
        even=getlongestpalindrome(string,i-1,i)
        Longest=max(odd,even,key=lambda x : x[1]-x[0])
        currentLongest=max(currentLongest,Longest,key=lambda x : x[1]-x[0])
    return string[currentLongest[0]:currentLongest[1]]

def getlongestpalindrome(string,leftidx,rightidx):
    while leftidx>=0 and rightidx< len(string):
        if string[leftidx] != string[rightidx]:
            break
        leftidx -= 1
        rightidx += 1
    print (string[leftidx+1:rightidx])
    print (leftidx,rightidx)
    return [leftidx+1,rightidx]


print (getlongestpalindromesubstring("babad"))
        
