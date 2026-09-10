# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
'''
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations


def permutationsHelper(array, currentPermutation, permutations):
    print ("inside permutationsHelper "+str(array), str(currentPermutation))
    if not len(array) and len(currentPermutation):
        print ("inside if array,currentPermutation "+str(array), str(currentPermutation))
        permutations.append(currentPermutation)
        print ("permutations: "+str(permutations))
    else:
        for i in range(len(array)):
            print ("inside else array,currentPermutation "+str(len(array)), str(currentPermutation))
            print ("i:"+str(i))
            newArray = array[:i] + array[i + 1 :]
            print ("newArray: "+str(newArray))
            newPermutation = currentPermutation + [array[i]]
            print ("newPermutation: "+str(newPermutation))
            permutationsHelper(newArray, newPermutation, permutations)

print (getPermutations([1,2,3]))
'''
# O(n*n!) time | O(n*n!) space
def getPermutations(array):
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations


def permutationsHelper(i, array, permutations):
    print ("inside permutationsHelper ")
    print ("i ,array, permutations "+str(i),str(array),str(permutations))
    if i == len(array) - 1:
        print ("inside If ")
        print ("i ,array, permutations "+str(i),str(array),str(permutations))
        permutations.append(array[:])
        print ("permutations.append "+str(permutations))
    else:
        print ("inside else ")
        print ("i ,array, permutations "+str(i),str(array),str(permutations))
        for j in range(i, len(array)):
            print ("j ,array, ,len(array), permutations "+str(j),str(array),str(len(array)),str(permutations))
            swap(array, i, j)
            print ("SWAP1 "+str(array))
            print ("calling permutationsHelper I+1, array , permutations"+str(i+1),str(array),str(permutations))
            permutationsHelper(i + 1, array, permutations)
            swap(array, i, j)
            print ("SWAP2 "+str(array))


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    
print (getPermutations([1,2,3]))
