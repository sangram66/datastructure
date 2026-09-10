'''
Caesar Cipher Encryptor
Given a non-empty string of lowercase letters and a non-negative integer value representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the letter "a".
Sample input: "xyz", 2 Sample output: "zab"
'''


#Solution 1
#o(n) Time |o(n) space
def ceaserCipherEncryptor(string, key):
    newLetter=[]
    newKey = key % 26
    print ("newkey:"+str(newKey))

    for letter in string:
        print ("letter:"+str(letter))
        newLetter.append(getNewLetter(letter,newKey))
    return "".join(newLetter)

def getNewLetter(letter,key):
    newLetterCode=ord(letter) + key 
    print ("newLetterCode:"+str(newLetterCode))
    return chr(newLetterCode) if newLetterCode <=122 else chr(96 + newLetterCode %122)

print(ceaserCipherEncryptor('xyz',25))  # (1,2)(a,b))  # (1,2)
'''

#Solution 2
#o(n) Time |o(n) space
def ceaserCipherEncryptor(string, key):
    newLetter=[]
    newKey = key % 26
    print ("newkey:"+str(newKey))
    alphabet = list ("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        print ("letter:"+str(letter))
        newLetter.append(getNewLetter(letter,newKey,alphabet))
        print (newLetter)
    return "".join(newLetter)

def getNewLetter(letter,newkey,alphabet):
    newLetterCode=alphabet.index(letter) + newkey 
    print ("newLetterCode:"+str(newLetterCode))
    return alphabet[newLetterCode] if newLetterCode <=25 else alphabet[-1 + newLetterCode % 25 ]

print(ceaserCipherEncryptor('xyz',25))  # (1,2)(a,b))  # (1,2)
'''