def reversei(x):
    temp = 0
    if x >= 0:
        temp = int(str(x)[::-1])
    else: 
        temp = -1*int(str(x)[1:][::-1])
            
    return temp if -2**31 <= temp <= 2**31 -1 else 0
    
print (reversei(1563847412))
        