import itertools
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    print (x)
                    yield x
        print (list(x == y for x, y in itertools.zip_longest(F(S), F(T))))
        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
    

s = "ab#c"
t = "ad#c"    
print (Solution().backspaceCompare(s,t))