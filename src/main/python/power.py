def mypow(x,n):
    def helper(x,n):
        if x ==0: return 0
        if n ==0: return 1
        print (x,n)
        res = helper(x,n//2)
        print (res,x,n)
        res = res * res 
        print ("ref")
        return (x * res) if n%2 else (res)
    
    res = helper(x,abs(n))
    print ("ref1")
    return (res) if n>=0 else (1/res)

print (mypow(2,10))