'''
def getlongestpalindromesubstring(string):
    currentLongest=[0,1]
    for i in range(1,len(string)):
        odd=getlongestpalindrome(string,i-1,i+1)
        even=getlongestpalindrome(string,i-1,i)
        Longest=max(odd,even,key=lambda x : x[1]-x[0])
        currentLongest=max(Longest,currentLongest,key=lambda x : x[1]-x[0])
    return string[currentLongest[0]:currentLongest[1]]

def getlongestpalindrome(string,leftidx,rightidx):
    while leftidx>=0 and rightidx< len(string):
        if string[leftidx] != string[rightidx]:
            break
        leftidx -= 1
        rightidx += 1
    return [leftidx+1,rightidx]


print (getlongestpalindromesubstring("abaxyzzyxf"))
'''
def getLongestpalindrome(string):
    resu=""
    for i in range(len(string)):
        #odd case
        tmp=getpalindrome(string,i-1,i+1)
        if len(tmp) > len(resu):
            resu=tmp
        #even case
        tmp=getpalindrome(string,i-1,i)
        if len(tmp) > len(resu):
            resu=tmp
    return resu

def getpalindrome(string,leftidx,rightidx):
    while leftidx>=0 and rightidx < len(string):
        if string[leftidx] != string[rightidx]:
            break
        else:
            leftidx -= 1
            rightidx +=1
    return string[leftidx+1:rightidx]
        
print (getLongestpalindrome("abaxyzzyxf"))
        