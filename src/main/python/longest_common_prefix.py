'''
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=[]
        minstr=min(strs,key=len)
        for i in range(len(minstr)):
            if all([minstr[i]==wd[i] for wd in strs ]):
                res.append(minstr[i])
            else:
                break
                
        return (''.join(res))
    
'''   
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=''
        for i in zip(*strs):
            
            print (i)
            if len(set(i))==1:
                res+=i[0]
            else:
                break
                
        return res
'''