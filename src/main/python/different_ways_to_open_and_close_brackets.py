'''
class Solution:
    def generateParenthesis(self, n: int) :
        
        def backtrack(ans, curr, openp, closep, maxp):
            print (ans,'----',curr,'----',str(openp),'----',str(closep),'----',str(maxp))
            if len(curr) == 2*maxp:
                ans.append(curr)
            if openp < maxp:
                backtrack(ans, curr+'(', openp+1, closep, maxp)
            if closep < openp:
                backtrack(ans, curr+')', openp, closep+1, maxp)
        
        ans = []
        openp, closep = 0, 0
        curr = ''
        backtrack(ans, curr, openp, closep, n)
        return ans
    
print (Solution().generateParenthesis(2))
'''
'''
[] ----  ---- 0 ---- 0 ---- 2
[] ---- ( ---- 1 ---- 0 ---- 2
[] ---- (( ---- 2 ---- 0 ---- 2
[] ---- (() ---- 2 ---- 1 ---- 2
[] ---- (()) ---- 2 ---- 2 ---- 2
['(())'] ---- () ---- 1 ---- 1 ---- 2
['(())'] ---- ()( ---- 2 ---- 1 ---- 2
['(())'] ---- ()() ---- 2 ---- 2 ---- 2
['(())', '()()']
'''
import sys

class Solution:
    def generateParenthesis(self, n) :
        
        res = []
        
        def inner(curr,l,r):
            print (curr,'----',str(l),'----',str(r))
            # if current string hit n*2
            # thats when you back out!
            if len(curr) == n*2:
                res.append(curr)
                return
            
            # keep adding left parens until no more remaining
            if l>0:
                #print ("calling left")
                inner(curr+"(",l-1,r)
                
            # keep adding right parens if a left matches it
            # and there are remaining
            if r>0 and l<r:
                #print ("calling right")
                inner(curr+")",l,r-1)
                    
        inner("",n,n)
        return res
'''    
def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    if event == 'call':
        print ('Call to %s on line %s of %s' % (func_name, line_no, filename))
        return trace_calls_and_returns
    elif event == 'return':
        print ('%s => %s' % (func_name, arg))
    return

sys.settrace(trace_calls_and_returns)
'''
print (Solution().generateParenthesis(3))

'''
 ---- 2 ---- 2
( ---- 1 ---- 2
(( ---- 0 ---- 2
(() ---- 0 ---- 1
(()) ---- 0 ---- 0
() ---- 1 ---- 1
()( ---- 0 ---- 1
()() ---- 0 ---- 0
['(())', '()()']
'''
