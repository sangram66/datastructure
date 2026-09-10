class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m,n=len(s),len(t)
        #print (m,n)
        if abs(m-n) > 1:
            #print ("false")
            return False
        count = 0 
        i,j=0,0
        while i < m and j < n :
            if s[i] != t[j]:
                #print (S[i],t[j])
                if count ==1:
                    return False 
                
                if m > n:
                    i+=1
                elif m < n:
                    j+=1
                else:
                    i+=1
                    j+=1
                    
                count+=1
            else:
                i+=1
                j+=1
                
        if i < m or j< n:
            count+=1
                
        return count ==1 
    
s1 = "gfg"
s2 = "gf"
if Solution().isOneEditDistance(s1, s2):
    print ("Yes")
else:
    print ("No")
 