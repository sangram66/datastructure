''''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
''' 
 
 
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        if len(A)>len(B): 
            A, B = B, A
        
        total = len(A) + len(B)
        lo = 0
        hi = len(A)
        while lo <= hi:
            # Find Partition in A using a regular binary search method. 
            midA    = (hi+lo)//2
            A_left  = A[midA-1] if midA   != 0    else float('-inf')
            A_right = A[midA]   if len(A) != midA else float('inf')
            
            # Partition index in B derived from A, and moves in opposite direction of Partition A
            # - Median Index is usually midway somewhere, so here should be ~ Total // 2. And we know that:
            # - midA + midB = Total // 2
            # - midB = Total // 2 - midA
            midB    = total//2 - midA       
            B_left  = B[midB-1] if midB   !=0      else float('-inf')            
            B_right = B[midB]   if len(B) != midB  else float('inf')

            if A_left <= B_right and B_left <= A_right:     # If both lefts are less than both rights, ideal partition detected.
                if total %2 == 0:
                    return max(A_left, B_left)/2.0 + min(A_right, B_right)/2.0
                else:
                    return min(A_right, B_right)                
            elif A_left > B_right:                          # A is too big   --> Reduce A partition size
                hi = midA-1
            elif A_left < B_right:                          # A is too small --> Increase A partition size (thereby reducing B)        
                lo = midA+1
        return None

a = [1, 2] 
b = [3, 4] 

print (Solution().findMedianSortedArrays(a,b))


'''
# Python code for median with   
# case of returning double 
# value when even number  
# of elements are present 
# in both array combinely 
median = 0
i = 0 
j = 0
   
# def to find max 
def maximum(a, b) : 
    return a if a > b else b 
   
# def to find minimum 
def minimum(a, b) : 
    return a if a < b else b 
   
# def to find median 
# of two sorted arrays 
def findMedianSortedArrays(a, n, b, m) : 
  
    global median, i, j 
    min_index = 0 
    max_index = n  
    print ("min_index,max_index "+str(min_index)+" , "+str(max_index))
       
    while (min_index <= max_index) : 
      
        i = int((min_index + max_index) / 2) 
        j = int(((n + m + 1) / 2) - i) 
        print ("i,j "+str(i)+" , "+str(j))
       
        # if i = n, it means that  
        # Elements from a[] in the 
        # second half is an empty  
        # set. and if j = 0, it  
        # means that Elements from  
        # b[] in the first half is  
        # an empty set. so it is  
        # necessary to check that,  
        # because we compare elements  
        # from these two groups.  
        # Searching on right 
        if (i < n and j > 0 and b[j - 1] > a[i]) : 
            min_index = i + 1
            print ("reached here1 min_index:"+str(min_index))
                   
        # if i = 0, it means that  
        # Elements from a[] in the 
        # first half is an empty  
        # set and if j = m, it means 
        # that Elements from b[] in  
        # the second half is an empty  
        # set. so it is necessary to 
        # check that, because we compare  
        # elements from these two groups. 
        # searching on left 
        elif (i > 0 and j < m and b[j] < a[i - 1]) : 
            max_index = i - 1
            print ("reached here2 max_index:"+str(max_index))
           
        # we have found the 
        # desired halves. 
        else : 
          
            # this condition happens when  
            # we don't have any elements  
            # in the first half from a[]  
            # so we returning the last 
            # element in b[] from the  
            # first half. 
            if (i == 0) : 
                median = b[j - 1] 
                print ("reached here3 median:"+str(median))
                   
            # and this condition happens  
            # when we don't have any  
            # elements in the first half  
            # from b[] so we returning the  
            # last element in a[] from the  
            # first half. 
            elif (j == 0) : 
                median = a[i - 1]    
                print ("reached here4 median:"+str(median))      
            else : 
                median = maximum(a[i - 1], b[j - 1])  
                print ("reached here5 median:"+str(median)) 
            break
          
      
       
    # calculating the median. 
    # If number of elements  
    # is odd there is  
    # one middle element. 
   
    if ((n + m) % 2 == 1) : 
        print ("1")
        return median 
   
    # Elements from a[] in the  
    # second half is an empty set.  
    if (i == n) : 
        print ("2")
        return ((median + b[j]) / 2.0) 
   
    # Elements from b[] in the  
    # second half is an empty set. 
    if (j == m) : 
        print ("3")
        print ( a[i])
        return ((median + a[i]) / 2.0) 
       
    return ((median + minimum(a[i], b[j])) / 2.0) 
  
   
# Driver code 
a = [1, 2] 
b = [3, 4] 
n = len(a) 
m = len(b) 
   
# we need to define the  
# smaller array as the  
# first parameter to make  
# sure that the time complexity 
# will be O(log(min(n,m))) 
if (n < m) : 
    print ("The median is : {}".format(findMedianSortedArrays(a, n, b, m))) 
else : 
    print ("The median is : {}".format(findMedianSortedArrays(b, m, a, n))) 
    
'''
  