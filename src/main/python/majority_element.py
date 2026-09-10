#https://leetcode.com/explore/interview/card/apple/344/array-and-strings/3112/
#below takes more than O(1) space since set is created
'''
def majority_element(arr):
    ans=[]
    for i in list(set(arr)):
        if arr.count(i) > len(arr)/3:
            ans.append(i)
    return ans

print (majority_element([1,1,1,3,3,2,2,2]))
'''
# Python 3 program to find if 
# any element appears more than
# n/3.
import sys
 
def appearsNBy3(arr, n):
 
    count1 = 0
    count2 = 0
    first = sys.maxsize
    second = sys.maxsize
    print (first,second)
 
    for i in range(0, n): 
 
        # if this element is
        # previously seen, 
        # increment count1.
        if (first == arr[i]):
            count1 += 1
 
        # if this element is
        # previously seen, 
        # increment count2.
        elif (second == arr[i]):
            count2 += 1
     
        elif (count1 == 0):
            count1 += 1
            first = arr[i]
 
        elif (count2 == 0):
            count2 += 1
            second = arr[i]
         
 
        # if current element is 
        # different from both
        # the previously seen 
        # variables, decrement
        # both the counts.
        else:
            count1 -= 1
            count2 -= 1
         
     
 
    count1 = 0
    count2 = 0
    print (first,second)
    res=''
    # Again traverse the array
    # and find the actual counts.
    for i in range(0, n): 
        if (arr[i] == first):
            count1 += 1
 
        elif (arr[i] == second):
            count2 += 1
    print (count1,count2) 
 
    if (count1 > n / 3):
        res+=str(first)
        #return first
 
    if (count2 > n / 3):
        res+=','+str(second)
        #return second
 
    if not res: 
        return -1
    else:
        return (res)
 
# Driver code
arr = [1,1,1,3,3,3,2,2,2]
n = len(arr) 
print(appearsNBy3(arr, n))
