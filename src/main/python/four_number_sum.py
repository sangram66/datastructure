'''

Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional 
array of all these quadruplets in no particular order. If no four numbers sum up to the target sum, 
the function should return an empty array.

Sample input: [7, 6, 4, -1, 1, 2], 16
Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]

inparr = [1,0,-1,0,-2,2]
sum = 0

'''
# Copyright © 2020 AlgoExpert, LLC. All rights reserved.

# Average: O(n^2) time | O(n^2) space
# Worst: O(n^3) time | O(n^2) space
def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = set()
    for i in range(1, len(array) - 1):
        print ("---i---- :"+str(i))
        for j in range(i + 1, len(array)):
            print ("---j---- :"+str(j))
            print ("array[i] + array[j] : "+str(array[i]),str(array[j]))
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            print ("currentSum + difference : "+str(currentSum),str(difference))
            print ("allPairSums :"+str(allPairSums))
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.add(tuple(sorted([pair[0],pair[1] , array[i], array[j]])))
                    print ("quadruplets :"+str(quadruplets))
        for k in range(0, i):
            print ("inside K")
            print ("array[i] + array[k] : "+str(array[i]),str(array[k]))
            currentSum = array[i] + array[k]
            print ("currentSum : "+str(currentSum))
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
                print ("inside k if  : "+str(allPairSums))
            else:
                allPairSums[currentSum].append([array[k], array[i]])
                print ("inside k else  : "+str(allPairSums))
    return quadruplets

#inparr=[5, -5, -2, 2, 3, -3]
#sum=0
inparr = [1,0,-1,0,-2,2]
sum = 0
print (fourNumberSum(inparr,sum))

