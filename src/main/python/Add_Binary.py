'''
Given two binary strings a and b, return their sum as a binary string.
Input: a = "1010", b = "1011"
Output: "10101"

'''

import itertools
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, carry = [], 0
        for x, y in itertools.zip_longest(reversed(a), reversed(b), fillvalue="0"):
            carry += (x == "1") + (y == "1")
            print (x,y,carry)
            carry, d = divmod(carry, 2)
            print (x,y,carry,d)
            ans.append(d)
            print(ans)
        if carry: ans.append(carry)
        print (ans)
        return "".join(map(str, reversed(ans)))
    
    
a = "1011"
b = "1011"
sol=Solution()
print (sol.addBinary(a,b))
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l=max(len(a),len(b))
        a=a.zfill(l)
        b=b.zfill(l)
        carry=0
        ans=[0]*(l)
        for i in range(l-1,-1,-1):
            su=0
            su=int(a[i])+int(b[i])+carry
            if su==3:
                carry=1
                ans[i]='1'
            elif su==2:
                carry=1
                ans[i]='0'
            elif su==1:
                carry=0
                ans[i]='1'
            elif su==0:
                carry=0
                ans[i]='0'
        return ('1'+(''.join(ans))if carry==1 else (''.join(ans)))

a = "1011"
b = "1011"
sol=Solution()
print (sol.addBinary(a,b))                
'''             