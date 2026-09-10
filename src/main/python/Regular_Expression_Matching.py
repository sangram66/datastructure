class Solution:
    def isMatch(self, s, p):
        memo = {}
        print ("memo: "+str(memo))
        def dp(si, pi):
            print ("inside dp")
            if pi >= len(p): print ("pi: "+str(pi)) ;return si == len(s)
            if si >= len(s): print ("si: "+str(si)) ;return pi + 1 < len(p) and p[pi + 1] == '*' and dp(si, pi + 2)
            if (si, pi) not in memo:
                matched = p[pi] == '.' or p[pi] == s[si]
                if pi + 1 < len(p) and p[pi + 1] == '*':
                    memo[(si, pi)] = dp(si, pi + 2) or (matched and dp(si + 1, pi))
                else:
                    memo[(si, pi)] = matched and dp(si + 1, pi + 1)
            return memo[(si, pi)]
        print ("start")
        return dp(0, 0)


s = "aa"
p = "a"
print (Solution().isMatch(s,p))