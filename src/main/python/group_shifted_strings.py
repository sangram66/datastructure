'''
249. Group Shifted Strings
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]
'''
from collections import defaultdict
class Solution:
    def groupStrings(self, strings) :
        '''
        Example:
        string  | signature
        ace     | 2.2  (storing diff between 'c'-'a'. 'e'.'c') 
        bdf     | 2.2  (storing diff between 'd'-'b'. 'f'.'d') 
        '''
        hmap = defaultdict(list) #key=signature:val [list of strings]
        
        
        for s in strings:
            if len(s) == 1:
                hmap[0].append(s)
            else:
                # find signature
                signature = ""
                for i in range(1,len(s)):
                    diff = ord(s[i]) - ord(s[i-1])
                    print (s,s[i],s[i-1],diff)
                    if diff >= 0:
                        signature += str(diff)
                    else:
                        signature += str(diff + 26) # take care when diff is negative
                    signature += '.'
                hmap[signature].append(s)
        print (hmap)
        

        res = []
        for key in hmap.keys():
            res.append(hmap[key])
            
        return res
    
print (Solution().groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
#print (Solution().groupStrings(["a"]))
        
        
            
        
    