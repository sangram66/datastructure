'''
def palindromeCheck(string):
    left=0
    right=len(string)-1
    while left < right:
        if string[left] != string[right]:
            return False
        else:
            left+=1
            right-=1
    return True


print (palindromeCheck("carrac"))
'''
def palindrome(string):
    cleansed_string=''.join(x for x in string if x.isalpha() or x.isdigit()).lower()
    rev_string=cleansed_string[::-1]
    print (cleansed_string)
    print (rev_string)
    if cleansed_string==rev_string:
        return True
    else:
        return False
    

print (palindrome("A man, a plan, a canal: Panama"))
#print (palindrome("race a car"))
    
        