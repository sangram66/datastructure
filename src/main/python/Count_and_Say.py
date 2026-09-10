class Solution(object):    
    def countAndSay(self, n):
        print ("before if n==1:  "+str(n))
        if n==1:
            return "1"
        s = self.countAndSay(n-1)
        print ("self.countAndSay(n-1)  "+str(n))
        print ("s  "+str(s))
        count, ans = 1, ""
        print ("count "+str(count))
        for i in range(len(s)-1):
            print ("Inside loop "+str(s[i])+'      '+str(s[i+1]))
            if s[i] == s[i+1]:
                count += 1
            else:
                ans += str(count) + s[i]
                count = 1
        ans += str(count) + s[-1]
        print ("ans  "+ans)
        return ans
if __name__=='__main__':  
    sol=Solution()
    print (sol.countAndSay(6))