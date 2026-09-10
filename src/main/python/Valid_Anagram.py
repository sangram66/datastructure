class Solution:
    '''
    def isAnagram(self, s, t):
    
        counter = {}
            
        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        
        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                return False
        for val in counter.values():
            if val != 0:
                return False

        return True
    '''
    def isAnagram(self, s, t):
        if s=="" and t=="":
            return True 
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        
        for ch in set(s):
            s_c = s.count(ch)
            t_c = t.count(ch)
            if s_c != t_c:
                return False 
        return True
            
    
sol=Solution()
s = "anagram"
t = "nagaram"
print (sol.isAnagram(s,t))