'''
Time Complexity: O(logn) 
Space Complexity: O(1)
'''
def _pow(base,power):
    if power == 1:
        return base
    
    y=_pow(base, power // 2)
    print ("base power y"+str(base),str(power),str(y))
    result=y*y
    print ("result1: "+str(result))
    
    if power%2:
        result *= base
    return result

def pow(x,n):
    if n==0:
        return 1
    if x==1:
        return 1
    if x==0:
        if n <0 :
            raise ZeroDivisionError('..')
        return 0
    if n < 0:
        power = -n
    else:
        power = n
        
    if x < 0:
        base = -x
    else:
        base = x
        
    result = _pow(base,power)
    print ("result "+str(result))
    if base != x and power %2:
        result = -result
        
    if power != n:
        result = 1/result
    
    return result
        

print(pow(-4,9))
        