'''

  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.

array=[10, 5, 9, 10, 12]
 opt [10, 10, 12]


array= [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

Sample Output [18, 141, 541]

'''


def findthreelargest(array):
    threelargest=[None,None,None]
    for num in array:
        updatethreelargest(threelargest,num)
    return threelargest
    
def updatethreelargest(threelargest,num):
    if threelargest[2] is None or num > threelargest[2]:
        updateandshift(threelargest,num,2)
    elif threelargest[1] is None or num > threelargest[1]:
        updateandshift(threelargest,num,1)
    elif threelargest[0] is None or num > threelargest[0]:
        updateandshift(threelargest,num,0)                
        
def updateandshift(threelargest,num,idx):
    for i in range(idx + 1 ):
        if i == idx:
            threelargest[i] = num
        else:
            threelargest[i] = threelargest[i+1]
array=[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7] 
print(findthreelargest(array))    
 