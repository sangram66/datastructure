
'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        s=s.lower()
        while i <= j :
            if not((ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 48 and ord(s[i]) <= 57)):
                i+=1
            elif not((ord(s[j]) >= 97 and ord(s[j]) <= 122) or (ord(s[j]) >= 48 and ord(s[j]) <= 57)) :
                j-=1
            elif s[i] == s[j]:
                i+=1
                j-=1
                
            else:
                return False 
            
        return True
    
print (Solution().isPalindrome('race a car'))
'''


def sentencePalindrome(s):
    l, h = 0, len(s) - 1
   
    # Lowercase string
    s = s.lower()
   
    # Compares character until they are equal
    while (l <= h):
   
        # If there is another symbol in left
        # of sentence
        if (not(s[l] >= 'a' and s[l] <= 'z')):
            l += 1
   
        # If there is another symbol in right
        # of sentence
        elif (not(s[h] >= 'a' and s[h] <= 'z')):
            h -= 1
   
        # If characters are equal
        elif (s[l] == s[h]):
            l += 1
            h -= 1
         
        # If characters are not equal then
        # sentence is not palindrome
        else:
            return False
    # Returns true if sentence is palindrome
    return True
   
# Driver program to test sentencePalindrome()
s = "race a car."
if (sentencePalindrome(s)):
    print ("Sentence is palindrome.")
else:
    print ("Sentence is not palindrome.")
'''