from math import floor 
class Solution:
    def intToRoman(self, num) :
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        
        powersOfTen = 0;
        currentDigit = floor( num % 10 )
        
        retStr = ""
        
        while num > 0: 
            if currentDigit < 5:
                if currentDigit == 4:
                    subtractor = ones[powersOfTen]
                    number = fives[powersOfTen]
                else:
                    subtractor = ""
                    number = ones[powersOfTen] * currentDigit
            if currentDigit == 5:
                subtractor = ""
                number = fives[powersOfTen]
            if currentDigit > 5:
                if currentDigit == 9:
                    subtractor = ones[powersOfTen]
                    number = ones[powersOfTen + 1]
                else:
                    subtractor = fives[powersOfTen]
                    number =   ones[powersOfTen] * ( currentDigit - 5 ) 
            retStr = subtractor + number + retStr;
            num = num // 10
            powersOfTen += 1
            currentDigit = floor( num % 10 )
        
        return retStr                    

sol=Solution()
print (sol.intToRoman(58))
