import sys
class Word(object): 
    def __init__(self, string, index): 
        self.string = string 
        self.index = index 

def printarray(arrays):
    for arr in arrays:
        print (arr.string, arr.index),
# Create a DupArray object that contains an array 
# of Words 
def createDupArray(string, size): 
    dupArray = [] 
  
    # One by one copy words from the given wordArray 
    # to dupArray 
    for i in range(size): 
        dupArray.append(Word(string[i], i)) 
    return dupArray 

# Given a list of words in wordArr[] 
def printAnagramsTogether(wordArr, size): 
    # Step 1: Create a copy of all words present in 
    # given wordArr. 
    # The copy will also have orignal indexes of words 
    dupArray = createDupArray(wordArr, size) 
    printarray(dupArray)
    print('\n')
    # Step 2: Iterate through all words in dupArray and sort 
    # individual words. 
    for i in range(size): 
        dupArray[i].string = ''.join(sorted(dupArray[i].string)) 
        print ("dupArray2 :"+str(list(dupArray)))
        printarray(dupArray)
        print('\n')
    

    # Step 3: Now sort the array of words in dupArray 
    dupArray = sorted(dupArray, key = lambda k: k.string) 
    print ("dupArray3 :"+str(list(dupArray)))
    printarray(dupArray)
    print('\n')
    
    res=[]
    curr=dupArray[1].string
    for word in dupArray:
        print (word.string)
        print (curr)
        print ("before if")
        print (wordArr[word.index])
        if word.string==curr:
            res.append(wordArr[word.index])
        else:
            print ("before else")
            print (res)
            print (word.string)
            res=[]
            res.append(wordArr[word.index])
            print (res)
            curr=word.string
            
        
  
    # Step 4: Now all words in dupArray are together, but 
    # these words are changed. Use the index member of word 
    # struct to get the corresponding original word 
    """
    res=[]
    pole=dupArray[1].string
    print ("pole :"+str(pole))
    for word in dupArray:
        print ("word: "+str(word.string))
        if word.string==pole:
            res.append(wordArr[word.index])
        else:
            pole=word.string
            print (pole)
            print (res)
    """

             

        
  
# Driver program 
wordArr = ["cat", "dog", "tac", "god", "act"] 
size = len(wordArr) 
printAnagramsTogether(wordArr, size) 