'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]

Space Complexity: O(n)
Time Complexity: O(n)
'''

import collections
class Solution:
    def partitionLabels(self, S) :
        #d={}
        d = collections.defaultdict(int)
        #print (list(d))
        print (list(enumerate(S)))
        for i, c in enumerate(S): d[c] = i
        
        print (d[c])
        print ("D "+str(list(d.items())))
        ans, left, right = [], -1, -1
        for i, c in enumerate(S):
            print (right,d[c])
            right = max(right, d[c])
            if i == right:
                ans.append(right-left)
                left = i
        return ans
    
sol=Solution()
print (sol.partitionLabels('ababcbacadefegdehijhklij'))
'''

from collections import Counter
class Solution:
    def partitionLabels(self, S) :
        
        all_counts = Counter(S)
        
        
        res = []
        left = 0
        
        counts, ref_counts = Counter(), Counter()
        
        for right, c in enumerate(S):
            counts[c] += 1
            if c not in ref_counts:
                ref_counts[c] = all_counts[c]
            
            if counts == ref_counts:
                res.append(right - left + 1)
                counts = Counter()
                ref_counts = Counter()
                left = right + 1
                
        return res
                        
  
sol=Solution()
print (sol.partitionLabels('ababcbacadefegdehijhklij'))
'''  