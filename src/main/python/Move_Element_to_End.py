'''
o(n) time | o(1) space
  You're given an array of integers and an integer. Write a function that moves
  all instances of that integer in the array to the end of the array and returns
  the array.


  The function should perform this in place (i.e., it should mutate the input
  array) and doesn't need to maintain the order of the other integers.

Sample Input = [2, 1, 2, 2, 2, 3, 4, 2]
toMove=2
Sample Output = [1, 3, 4, 2, 2, 2, 2, 2] 
the numbers 1, 3, and 4 could be ordered differently

'''
def movelementstoend(array,tomove):
    idxstart=0
    idxend=len(array)-1
    while idxstart < idxend:
        while idxstart < idxend and array[idxend] == tomove:
            idxend-=1
        if array[idxstart] == tomove:
            array[idxstart],array[idxend] = array[idxend],array[idxstart]
        idxstart+=1
    return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove=2
print (movelementstoend(array,toMove))