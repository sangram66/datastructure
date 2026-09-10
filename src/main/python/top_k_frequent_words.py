from collections import defaultdict
class Solution:
    def topKFrequent(self, words, k):
        freq_map = defaultdict(int)
        res=[]
        for word in words:
            freq_map[word] += 1
        print (freq_map.items())
            
        #return sorted(freq_map, key = lambda k: (-freq_map[k], k))[:k]
        return sorted(freq_map, key = lambda k: (-freq_map[k]))[:k]


Input= ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 3
'''
Input= ["a", "aa", "aaaa"]
k = 1
'''  
print (Solution().topKFrequent(Input,k))
    
