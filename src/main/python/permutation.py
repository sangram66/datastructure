
'''
def getPermutations(array):
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations


def permutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationsHelper(i + 1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
'''
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations


def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
        print ("inside if "+str(permutations))
    else:
        print ("inside else "+str(array))
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1 :]
            newPermutation = currentPermutation + [array[i]]
            print ("inside else newArray,newPermutation "+str(newArray),str(newPermutation))
            permutationsHelper(newArray, newPermutation, permutations)
            print ("after completing newArray,newPermutation "+str(newArray),str(newPermutation))



print (getPermutations([1,2]))