'''
# Best: O(nlog(n)) time | O(nlog(n)) space
# Average: O(nlog(n)) time | O(nlog(n)) space
# Worst: O(nlog(n)) time | O(nlog(n)) space
def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray
'''
# Copyright © 2020 AlgoExpert, LLC. All rights reserved.

# Best: O(nlog(n)) time | O(n) space
# Average: O(nlog(n)) time | O(n) space
# Worst: O(nlog(n)) time | O(n) space
def mergeSort(array):
    if len(array) <= 1:
        return array
    auxiliaryArray = array[:]
    print ("auxiliaryArray in mergeSort"+str(auxiliaryArray))
    mergeSortHelper(array, 0, len(array) - 1, auxiliaryArray)
    return array


def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray):
    print ("inside mergeSortHelper mainArray, startIdx, endIdx, auxiliaryArray "+str(mainArray),str(startIdx),str(endIdx),str(auxiliaryArray))
    if startIdx == endIdx:
        return
    middleIdx = (startIdx + endIdx) // 2
    print ("middleIdx "+str(middleIdx))
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
    mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray)
    doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)


def doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
    print (" in side doMerge mainArray, startIdx,middleIdx, endIdx, auxiliaryArray "+str(mainArray),str(startIdx),str(middleIdx),str(endIdx),str(auxiliaryArray))
    k = startIdx
    i = startIdx
    j = middleIdx + 1
    print ("Inside do merge k,i,j"+str(k),str(i),str(j))

    while i <= middleIdx and j <= endIdx:
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            mainArray[k] = auxiliaryArray[i]
            i += 1
        else:
            mainArray[k] = auxiliaryArray[j]
            j += 1
        k += 1
    while i <= middleIdx:
        mainArray[k] = auxiliaryArray[i]
        i += 1
        k += 1
    while j <= endIdx:
        mainArray[k] = auxiliaryArray[j]
        j += 1
        k += 1


array=[8, 5, 2, 9, 5, 6, 3]
print (mergeSort(array))