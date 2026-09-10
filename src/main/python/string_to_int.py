class Solution:
    def myAtoi(self, s: str) -> int:  
        read=""
        isnegative=False
        isPositive=False
        s=s.lstrip(' ')
        #print (s)
        if not s:
            return 0
        
        if s[0]=='-':
            isnegative=True
            s=s[1:]
        elif  s[0]=='+':
            isPositive=True
            s=s[1:]
            
            
        for i in s:
            if i.isdigit():
                read+=i
                
            else:
                print ("break")
                break
        print ("hell0"+read)
        if read:
            read=read.lstrip('0')
            if read.isdigit():
                read = int(read)
            else:
                return 0 
        else:
            return 0 
        print (read)
        if isnegative:
            read*=-1
        if read < (2 ** 31)*-1:
            read = (2 ** 31)*-1
        elif read > ((2 ** 31) - 1):
            read = ((2 ** 31) - 1)    
        return (read)
    
    
print (Solution().myAtoi("words and 987"))
            