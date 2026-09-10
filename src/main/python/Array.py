#!/bin/python3
"""
import math
import os
import random
import re
import sys
from sys import maxsize 

# Complete the maxSubarray function below.
def maxSubarray(a):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    max_sub_squence=0
    start = 0
    end = 0
    s = 0
    size=len(a)
    for i in range(0,size): 
        print ("index :"+str(i))
        print ("max_so_far :"+str(max_so_far))
        print ("max_ending_here :"+str(max_ending_here))
        print ("value :"+str(a[i]))
        max_ending_here += a[i] 
        print ("max_ending_here :"+str(max_ending_here))
        print ("------------------------------------------")
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            max_sub_squence = max_ending_here
            start = s 
            end = i 
    
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
    print (max_so_far ) 
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(raw_input())

        arr = list(map(int, raw_input().rstrip().split()))

        result = maxSubarray(arr)
 """       
        
def arrayman(n,queries):
    diffarr = [0 for i in range(n+1)]
    for i in queries:
        diffarr[i[0]-1] += i[2]
        diffarr[i[1]]+= i[2]
    maximum=0
    tsum=0
    
    
    
import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr=[0]*n
    for i in queries:
        fr=queries[0]
        to=queries[1]
        ad=queries[2]
        for j in range(fr,to):
            arr[j]+=ad
    
    print (arr)

if __name__ == '__main__':

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, raw_input().rstrip().split())))

    result = arrayManipulation(n, queries)


