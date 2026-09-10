class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        print (" string passed :"+s)
        if s[0] == "0":
            return 0
        
        dp = [0] * (len(s) + 1)
        print ("all dp :" +str(dp))
        dp[0] = 1
        print (" dp[0] :" +str(dp))
        
        for i in range(1, len(s) + 1):
            print ("i :"+str(i))
            if 1 <= int(s[i - 1]) <= 9:
                print ("string :"+str(s[i - 1]))
                dp[i] += dp[i - 1]
                print ("inside for 1 to 9 :"+str(dp))
            if i > 1:
                if 10 <= int(s[i- 2] + s[i - 1]) <= 26:
                    print ("string in i>1 :"+str(s[i- 2] + s[i - 1]))
                    dp[i] += dp[i - 2]
                    print ("inside 10-26  dp :"+str(dp))
        
        return dp[-1]

if __name__=='__main__':
    sol=Solution()   
    s = "226"
    print (sol.numDecodings(s))