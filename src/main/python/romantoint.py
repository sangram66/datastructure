"""
class Solution:
    def romanToInt(self, s):
            d = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}        
            val = 0
            s = s[::-1]
            print ("s  "+str(s))
            val += d[s[0]]
            print ("val  "+str(val))
            for i in range(1,len(s)):
                print ("d[s[i]] , d[s[i-1]]  "+str(d[s[i]])+ '   ,     '+str(d[s[i-1]]))
                if d[s[i]] < d[s[i-1]]:
                    val -= d[s[i]]
                    print ("Inside if  val "+str(val))
                else:
                    val += d[s[i]]
                    print ("Inside else  val "+str(val))           
            return val
"""
"""
class Solution:
    def romanToInt(self, s):
            d = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}        
            val = 0
            #s = s[::-1]
            print ("s  "+str(s))
            val += d[s[0]]
            print ("val  "+str(val))
            for i in range(1,len(s)):
                print ("d[s[i]] , d[s[i-1]]  "+str(d[s[i]])+ '   ,     '+str(d[s[i-1]]))
                if d[s[i]] < d[s[i-1]]:
                    val += d[s[i]] 
                    print ("Inside if  val "+str(val))
                else:
                    val -= d[s[i]]
                    print ("Inside else  val "+str(val))           
            return val
           
if __name__=='__main__':
    sol=Solution()
    print (sol.romanToInt('VIII'))
""" 

"""  
class solution():
    def romantoint(self,num):
        d = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        i=0
        res=0
        while (i < len(num)):
            print (res,i)
            s1 = d[num[i]]
            if (i+1 < len(num)):
                s2 = d[num[i+1]]
                if s1 > s2:
                    res=res+s1
                    i=i+1
                else:
                    res=res+s2-s1
                    i=i+2
            else:
                res=res+s1
                i=i+1
        return (res)


print (solution().romantoint("VIII"))
"""    


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
        total = values[s[-1]]
        for i in reversed(range(len(s) - 1)):
            print (i,values[s[i]] , values[s[i + 1]])
            print (total)
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
                      

if __name__=='__main__':
    sol=Solution()
    print (sol.romanToInt('MMMDCCXXIV'))              
        
        