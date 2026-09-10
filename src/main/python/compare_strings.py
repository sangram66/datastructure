'''
compare two strings without using upper or lower libraries
'''

#from __builtin__ import False, True
def case_insensitive_compare(s1,s2):
    if len(s1) != len(s2):
        return False
    s1_iter = iter(s1)
    s2_iter = iter(s2)
    for _ in range(len(s1)):
        s1_c = s1_iter.next()
        s2_c = s2_iter.next()
        if not s1_c.upper() == s2_c.upper():
            return False
    return True

print (case_insensitive_compare('abc','AbC'))