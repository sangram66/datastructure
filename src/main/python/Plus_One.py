class Solution(object):
    def plusOne(self, digits):
        #res = []
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            print ("inside while:" +str(digits))
            i -= 1
            print ("inside while:" +str(i))
        if i == -1:
            print ("inside i == -1:" +str(i))
            return [1] + digits
        
        digits[i] += 1
        print ("outside while:" +str(digits)) 
        return digits

if __name__=='__main__':
    sol=Solution()
    Input= [9,9,9]
    print (sol.plusOne(Input))
    