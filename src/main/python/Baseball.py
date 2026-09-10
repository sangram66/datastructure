class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = 0
        stack = []
        print (stack)
        for c in ops:
            if c.isdigit():
                stack.append(int(c))
                print (" if is digit: "+str(stack))
                res += stack[-1]
            elif c == "+":
                stack.append(stack[-1]+stack[-2])
                print (" if is +: "+str(stack))
                res += stack[-1]
            elif c == "D":
                stack.append(2*stack[-1])
                print (" if is D: "+str(stack))
                res += stack[-1]
            else:
                res -= stack.pop()
                print (" if is C: "+str(stack))
        return res
    
ops=["5","2","C","D","+"]
print (Solution().calPoints(ops))