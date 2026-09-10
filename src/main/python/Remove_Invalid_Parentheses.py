class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(i, left, right, left_rem, right_rem, expr):
            print ("inside dfs")
            if i == len(s):
                if left_rem == right_rem:
                    res.add("".join(expr))
            else:
                if s[i] == "(":
                    expr.append("(")
                    print ("dfs : 1 ")
                    print (i+1, left+1, right, left_rem, right_rem, str(expr))
                    dfs(i+1, left+1, right, left_rem, right_rem, expr)
                    x=expr.pop()
                    print ("expr : 1 "+str(expr))
                    if left_rem > 0:
                        print ("dfs : 2 ")
                        print (i+1, left, right, left_rem-1, right_rem, str(expr))
                        dfs(i+1, left, right, left_rem-1, right_rem, expr)
                elif s[i] == ")":
                    if left > right:
                        expr.append(")")
                        print ("dfs : 3 ")
                        print (i+1, left, right+1, left_rem, right_rem, str(expr))
                        dfs(i+1, left, right+1, left_rem, right_rem, expr)
                        expr.pop()
                        print ("expr : 3 "+str(expr))
                    if right_rem > 0:
                        print ("dfs : 4 ")
                        print (i+1, left, right, left_rem, right_rem-1, str(expr))
                        dfs(i+1, left, right, left_rem, right_rem-1, expr)
                else:
                    expr.append(s[i])
                    print ("dfs : 5 ")
                    print (i+1, left, right, left_rem, right_rem, str(expr))
                    dfs(i+1, left, right, left_rem, right_rem, expr)
                    expr.pop()
                    print ("expr : 4 "+str(expr))
        
        res = set()
        left_rem = 0
        right_rem = 0
        for char in s:
            if char == "(":
                left_rem += 1
            elif char == ")":
                if left_rem <= 0:
                    right_rem += 1
                else:
                    left_rem -= 1
        print ('left_rem, right_rem: '+str(left_rem)+'  '+str(right_rem))
        dfs(0, 0, 0, left_rem, right_rem, [])
        return list(res)
    
opt=Solution().removeInvalidParentheses("()())()")
print (opt)