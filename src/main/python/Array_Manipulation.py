#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    diffArr=[0]*(n+1)    
    for i in (queries):
        print (i)
        print (diffArr[i[0]-1])
        diffArr[i[0]-1]+= i[2]
        print (diffArr)
        diffArr[i[1]]-= i[2]
        print (diffArr)
    maximum=0
    tsum=0
    for i in diffArr:
        tsum+=i
        if tsum > maximum:
            maximum=tsum
    return maximum
            
if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print (result)