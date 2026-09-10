import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n == 3**round(math.log(n,3))
    
#this formula is good to find if a number is power of an integer
#https://stackoverflow.com/questions/1804311/how-to-check-if-an-integer-is-a-power-of-3/1804399
