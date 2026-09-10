
import collections
import os
'''
class Solution(object):
    @profile
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        destDict = collections.defaultdict(list)
        for i, item in enumerate(B):
            destDict[item] = i
        
        print (destDict)
        
        res = []
        for key in A:
            res.append(destDict[key])
            
        return res
    
sol=Solution()
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
print (sol.anagramMappings(A,B))
'''
class Solution(object):
    def anagramMappings(self, A, B) :
        indices = collections.defaultdict(list)
        #print list(enumerate(B))
        for i, v in enumerate(B):
            indices[v].append(i)
        print (indices)
        return [indices[v].pop(0) for v in A]
sol=Solution()
A = [12, 28, 46, 32, 50, 46]
B = [50, 12, 32, 46, 28, 46]
print (sol.anagramMappings(A,B))




