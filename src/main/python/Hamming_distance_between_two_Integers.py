def hammingDistance(x, y) : 
  
    if x == y:
        return 0
        
    temp = x^y
    ans=0
        
    while (temp != 0):
        if (temp & 1) :
            ans+=1
        temp >>= 1
        
    return ans
  
if __name__=='__main__': 
    n1 = 9
    n2 = 14
    print(hammingDistance(1, 4)) 