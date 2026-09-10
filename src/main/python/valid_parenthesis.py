#https://leetcode.com/problems/valid-parentheses/
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
'''
class solution:
    def isValid(self, s):
            if not len(s): return True
            pairs = {
                "}": "{",
                ")" : "(",
                "]" : "["
            }
            openers = []
        
            for paren in s:
                print ("paren: "+str(paren))
                if paren in ("{[("): 
                    openers.append(paren)
                    print ("openers "+str(openers))
                elif len(openers) == 0:
                    return False
                    print ("Inside else")
                    print ("pairs[paren] : " + str(pairs[paren]))
                elif openers.pop() != pairs[paren]:
                    return False
            return len(openers) == 0

    
print (solution().isValid("()[]{}("))
'''
#o(n) time | o(n) space
def balancedbrackets(string):
    if not len(string): return True
    openbracket="[{("
    closebracket=")}]"
    pairs = {
                "}": "{",
                ")" : "(",
                "]" : "["
            }
    stack=[]
    for char in string:
        #print ("processing :"+char)
        if char in openbracket:
            stack.append(char)
            print (stack)
            #print ("stack append :"+str(stack))
        elif char in closebracket:
            #print ("sstack[-1] :"+str(stack[-1]))
            if len(stack) == 0:
                #print ("stack len check :"+str(stack))
                return False
            elif stack[-1] == pairs[char] :
                stack.pop()
                #print ("stack pop :"+str(stack))
            else:
                return False
    return len(stack)==0

                
        
#print (balancedbrackets("(((((({{{{{[[[[[([)])]]]]]}}}}}))))))"))   
print (balancedbrackets("[([])]"))    
 
    





