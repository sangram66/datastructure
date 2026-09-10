'''
Three Number Sum
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. 
The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold. If no three numbers sum up to the target sum, the function should return an empty array.

Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0 
Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
'''
def tripletSum(array,targetSum):
    array.sort()
    triplets=[]
    for curr in range(len(array)-2):
        left = curr+1
        right = len(array) -1
        while left < right :
            if array[curr] + array[left] + array[right] == targetSum:
                triplets.append([array[curr] , array[left] , array[right]])
                left += 1
                right -= 1
            elif array[curr] + array[left] + array[right] < targetSum:
                left += 1
            elif array[curr] + array[left] + array[right] > targetSum:
                right -= 1
    return triplets

print (tripletSum([12, 3, 1, 2, -6, 5, -8, 6],0))
            
        