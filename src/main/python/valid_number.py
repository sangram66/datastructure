'''
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
"-53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
'2e-0' => true
"-e.05" => false
'''
class Solution(object):
    def isNotdigit(self, s):
        return s.isdecimal() == False and s != ''

    def validleft(self, s):
        if '.' in s:
            count = s.split('.')
            if len(count) != 2 or self.isNotdigit(count[0]) or self.isNotdigit(count[1]) or (count[0] == '' and count[1] == ''):
                return False
            return True
        else:
            return s.isdecimal()

    def validright(self, s):
        count = s.split('e')
        if self.isflag(count[1]):
            count[1] = count[1][1:]
        if len(count) != 2 or self.validleft(count[0]) == False or count[1].isdecimal() == False:
            return False
        else:
            return True

    def isflag(self, s):
        return len(s) != 0 and (s[0] == '+' or s[0] == '-')

    def isNumber(self, s):
        s = s.strip()
        if self.isflag(s):
            s = s[1:]
        if 'e' not in s:
            return self.validleft(s)
        else:
            return self.validright(s)
    
if __name__ == "__main__":
    sol=Solution()
    s="-2.5e5"
    print (sol.isNumber(s))
    