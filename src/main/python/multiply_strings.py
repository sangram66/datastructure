def multiplystrings(s1,s2):
    totalsum,sum = 0,0
    for i in range(len(s1)):
        sum = 0
        for j in range(len(s2)):
            sum *= 10
            print (int(s1[i]) , int(s2[j]))
            sum += int(s1[i]) * int(s2[j])
        print ("totalsum: "+str(totalsum))
        print ("sum: "+str(sum))
        totalsum *= 10
        totalsum += sum
    print(totalsum)
"""    
s1='193283492420348904832902348908239048823480823'
s2='3248234890238902348823940990234'
multiplystrings(s1,s2)
"""
multiplystrings('22','11')


'''

class Solution:
    def multiply(self, num1, num2) :
        return str((self.convert(num1,len(num1))*self.convert(num2,len(num2))))
        
        
    def convert(self,num,len_num):
        valmap={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        n=0
        res=0
        while (len_num>0):
            res+=valmap[num[n]] * (10**(len_num-1))
            n=n+1
            len_num=len_num-1
        return (res)
            
'''