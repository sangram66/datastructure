'''
  Write a function that takes in two non-empty arrays of integers, finds the
  pair of numbers (one from each array) whose absolute difference is closest to
  zero, and returns an array containing these two numbers, with the number from
  the first array in the first position.


  You can assume that there will only be one pair of numbers with the smallest
  difference.
  
  arayone = [-1, 5, 10, 20, 28, 3]
  arraytwo  = [26, 134, 135, 15, 17]
  
  output =[28, 26]

'''
def smallestdifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float('inf')
    current = float('inf')
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if secondNum > firstNum:
            current = secondNum - firstNum
            idxOne += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            idxTwo += 1
        else :
            return [firstNum,secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum,secondNum]
    return smallestPair

arayone = [-1, 5, 10, 20, 28, 3]
arraytwo  = [26, 134, 135, 15, 17]
print (smallestdifference(arayone,arraytwo))