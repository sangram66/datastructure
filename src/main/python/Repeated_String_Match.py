#https://leetcode.com/explore/featured/card/google/67/sql-2/469/
class Solution:
    def repeatedStringMatch(self, A, B):
        C = ""
        for i in range(len(B)/len(A) + 3): 
            if B in C:
                return i
            C += A
        return -1
    
if __name__=='__main__':
    sol=Solution()
    print (sol.repeatedStringMatch("abcd" ,"cdabcdab"))
