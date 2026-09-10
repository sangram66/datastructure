# Copyright © 2020 AlgoExpert, LLC. All rights reserved.

# Best: O(nlog(n)) time | O(log(n)) space
# Average: O(nlog(n)) time | O(log(n)) space
# Worst: O(n^2) time | O(log(n)) space
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    print ("pivotIdx:" +str(pivotIdx))
    print ("leftIdx:" +str(leftIdx))
    print ("rightIdx:" +str(rightIdx))
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
            print ("inside 1st IF:" +str(array))
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
            print ("inside 2nd IF [leftIdx]:" +str(leftIdx))
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
            print ("inside 2nd IF [rightIdx]:" +str(rightIdx))
    swap(pivotIdx, rightIdx, array)
    print ("outside IF swap:" +str(array))
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    print ("leftSubarrayIsSmaller:" +str(leftSubarrayIsSmaller))
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        print ("inside if leftSubarrayIsSmaller first sort:" +str(array))
        quickSortHelper(array, rightIdx + 1, endIdx)
        print ("inside if leftSubarrayIsSmaller second sort:" +str(array))
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        print ("inside else leftSubarrayIsSmaller first sort:" +str(array))
        quickSortHelper(array, startIdx, rightIdx - 1)
        print ("inside else leftSubarrayIsSmaller first sort:" +str(array))


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print (quickSort([8,5,2,9,5,6,3]))