def Substr(Str, target):
     
    t = 0
    Len = len(Str)
    i = 0
     
    # Iterate from 0 to Len - 1
    for i in range(Len):
        if (t == len(target)):
            break
        if (Str[i] == target[t]):
            t += 1
        else:
            t = 0
             
    if (t < len(target)):
        return -1
    else:
        return (i - t)
 
# Driver code
print(Substr("GeeksForGeeks", "Fr"))
print(Substr("GeeksForGeeks", "For"))
print(Substr("abc", "c"))
 
