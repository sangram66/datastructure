'''
#consumes more time
def getNthfibonacci(n):
    lasttwo=[0,1]
    ctr=3
    while ctr <= n:
        nextfib = lasttwo[0] +lasttwo[1]
        lasttwo[0],lasttwo[1] =lasttwo[1],nextfib
        ctr+=1
    return lasttwo[1] if n>1 else lasttwo[0]


print (getNthfibonacci(13))
'''


#consumes more time
def getNthfibonacci(n):
    if n < 2: return n
    
    val0,val1,val2=0,1,0
    for i in range(2,n+1):
        val2=val0+val1
        val0,val1=val1,val2
    return val2

print (getNthfibonacci(13))
