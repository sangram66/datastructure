'''
https://www.algoexpert.io/questions/Validate%20Subsequence
  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers [1, 3, 4]  form a subsequence of the array [1, 2, 3, 4]
  , and so do the numbers [2, 4] . Note
  that a single number in an array and the array itself are both valid
  subsequences of the array.
  
  array  = [5, 1, 22, 25, 6, -1, 8, 10]
  sequence  = [1, 6, -1, 10]

 Output = True
'''

'''
def validsubsequence(array,sequence):
    arrIdx=0
    seqIdx=0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)
'''
def validsubsequence(array,sequence):
    seqIdx=0
    for value in array:
        if seqIdx == len(sequence):
            return True
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
        
        

array = [5,1,22,25,6,-1,8,10,11,12,13,14]
sequence = [1,6,-1,10]
print (validsubsequence(array,sequence))