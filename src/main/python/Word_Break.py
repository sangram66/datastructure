#https://leetcode.com/problems/word-break/
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
class Solution:
    def wordBreak(self, s, wordDict):
            """
            :type s: str
            :type wordDict: List[str]
            :rtype: bool
            """
            wordDict = set(wordDict)
            # c is candidate set, stores indicies of known valid words up to that point
            c = [0]
            for i in range(1, len(s)+1):
                print ("----------------i: "+str(i))
                for j in range(len(c)):
                    print ("j: "+str(j))
                    print ("i: "+str(i))
                    print ("c[j]: "+str(c[j]))
                    tmp = s[c[j]:i]
                    print ("tmp: "+str(tmp))
                    if tmp in wordDict:
                        # Last index to check, if we get a valid case here we
                        # immediately return True
                        if i == len(s):
                            return True
                        c.append(i)
                        print ("inside if tmp array c"+str(c))
                        # Short cut this loop. If we found a valid case its enough 
                        # to stop. Consider the case "aaaaaaa" ["a"]
                        break
            # Didnt pass on the last index
            return False
""" 
s = "applepenapple"
wordDict = ["apple", "pen"] 
print (Solution().wordBreak(s,wordDict))
"""

s = "leetcode"
wordDict = ["leet", "code"]             
print (Solution().wordBreak(s,wordDict))
'''

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]           
print (Solution().wordBreak(s,wordDict))
'''
