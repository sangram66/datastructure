'''
1554. Strings Differ by One Character
Medium

110

2

Add to List

Share
Given a list of strings dict where all the strings are of the same length.

Return true if there are 2 strings that only differ by 1 character in the same index, otherwise return false.

 

Example 1:

Input: dict = ["abcd","acbd", "aacd"]
Output: true
Explanation: Strings "abcd" and "aacd" differ only by one character in the index 1.
Example 2:

Input: dict = ["ab","cd","yz"]
Output: false
Example 3:

Input: dict = ["abcd","cccc","abyd","abab"]
Output: true


'''

class Solution:
    def differByOne(self, dict):
        combos = set()
        for key in dict:
            for i in range(len(key)):
                combo = key[:i] + '*' + key[i+1:]
                if combo in combos:
                    return True
                combos.add(combo)
        return False
    
dict = ["abcd","acbd", "aacd"]
print (Solution().differByOne(dict))