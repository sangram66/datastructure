#Time complexity : O(N)
#Space Complexity : O(1)

# Python program to check whether it is possible to make
# string palindrome by removing one character
 
# Utility method to check if substring from
# low to high is palindrome or not.
def isPalindrome(string: str, low: int, high: int) -> bool:
    print (string[low:high+1],low,high)
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True
 
# This method returns -1 if it
# is not possible to make string
# a palindrome. It returns -2 if
# string is already a palindrome.
# Otherwise it returns index of
# character whose removal can
# make the whole string palindrome.
def possiblepalinByRemovingOneChar(string: str) -> int:
 
    # Initialize low and right by
    # both the ends of the string
    low = 0
    high = len(string) - 1
 
    # loop untill low and high cross each other
    while low < high:
 
        # If both characters are equal then
        # move both pointer towards end
        if string[low] == string[high]:        
            low += 1
            high -= 1
        else:
 
            # If removing str[low] makes the whole string palindrome.
            # We basically check if substring str[low+1..high] is
            # palindrome or not.
            print ( "low: " +string[low:high+1])
            if isPalindrome(string, low + 1, high):
                return low
 
            # If removing str[high] makes the whole string palindrome
            # We basically check if substring str[low+1..high] is
            # palindrome or not
            print ("high:"+string[low:high+1])
            if isPalindrome(string, low, high - 1):
                
                return high
            return -1
 
    # We reach here when complete string will be palindrome
    # if complete string is palindrome then return mid character
    return -2
 
# Driver Code
if __name__ == "__main__":
 
    string = "aeaxabea"
    idx = possiblepalinByRemovingOneChar(string)
 
    if idx == -1:
        print("Not possible")
    elif idx == -2:
        print("Possible without removig any character")
    else:
        print("Possible by removing character at index", idx)
        
        
'''
If question is to just print true or false 


class Solution:
    def removeacharpalind(self,s,low,high):
        while low < high:
            if s[low] != s[high]:
                return False
            low +=1 
            high -=1
        return True
    def validPalindrome(self, s: str) -> bool:
        low=0
        high=len(s)-1
        while low < high :
        
            if s[low] == s[high]:
                low+=1
                high-=1
            
            else:
                if self.removeacharpalind(s,low+1,high):
                    return True
                if self.removeacharpalind(s,low,high-1):
                    return True
                return False 
        return True
        
        
'''
        
'''
def validpalindrome(s):
    l,r=0,len(s)-1
    while l < r:
        if s[l] != s[r]:
            skipL,skipR = s[l+1:r+1],s[l:r]
            return (skipL == skipL[::-1] or skipR == skipR[::-1])
        l,r = l+1, r-1
    return True 

print (validpalindrome("acebgca"))
        
        
'''