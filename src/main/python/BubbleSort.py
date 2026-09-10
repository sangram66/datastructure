'''
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the array.
Sample input: [8, 5, 2, 9, 5, 6, 3] Sample output: [2, 3, 5, 5, 6, 8, 9]
'''

#best : o(n) | o(1) space
#Average : o(n^2) time | o(1) space
#Wprst: o(n^2) time | 0(1) space

def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False 
        counter += 1 
    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]

array=[2, 1]
print bubbleSort(array)
