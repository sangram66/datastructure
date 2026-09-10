'''
https://www.algoexpert.io/questions/Two%20Number%20Sum

  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.


  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.


  You can assume that there will be at most one pair of numbers summing up to
  the target sum.

array = [3, 5, -4, 8, 11, 1, -1, 6] 
targetSum = 10 

Sample Output = [-1, 11] 
'''

#o(n) time | o(1) space 
#def twoNumberSum(array,targetSum):
#    array.sort()
#    l=0
#    r=len(array)-1
#    while l < r :
#        if array[l] + array[r] > targetSum:
#            r-=1
#        elif array[l] + array[r] < targetSum:
#            l+=1
#        elif  array[l] + array[r] == targetSum:
#            return [array[l] , array[r]]
#    else:
#        return []
#            
#a = [2,15,1,7]
#t = 9
#print(twoNumberSum(a,t))

#o(n) time | o(n) space 
def twonumsum(arr,tgt):
    vis={}
    res=[]
    for i in range(len(arr)):
        diff = tgt - arr[i]
        print (diff) 
        if diff in vis:
            res.append([arr[i],diff])
        else:
            vis[arr[i]]=i
            
    print (vis)
            
    return res 

a = [2,15,1,7]
t = 9
print(twonumsum(a,t))





