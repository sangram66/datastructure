def hasSingleCycle(array):
    # Write your code here.
    numElementsVisited=0
    currentdx=0
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentdx == 0:
            return False
        numElementsVisited += 1
        currentdx = getNextIndx(currentdx,array)
    return currentdx == 0

def getNextIndx(currentdx,array):
    jump = array[currentdx]
    print (currentdx,array,jump)
    nextIdx = (currentdx + jump) % len(array)
    print (nextIdx)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)


array=[10, 11, -6, -23, -2, 3, 88, 909, -26]
print (hasSingleCycle(array))