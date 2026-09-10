def kadane(a): 
    n = len(a) 
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, n): 
        max_ending_here = max_ending_here + a[i] 
        if (max_ending_here < 0): 
            max_ending_here = 0
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here
    print("max_so_far :"+str(max_so_far))        
    return max_so_far 
  
# The function returns maximum circular contiguous sum in 
# a[] 
def maxCircularSum(a): 
  
    n = len(a) 
  
    # Case 1: get the maximum sum using standard kadane's 
    # algorithm 
    max_kadane = kadane(a) 
    print("max_kadane :"+str(max_kadane))
    # Case 2: Now find the maximum sum that includes corner 
    # elements. 
    max_wrap = 0
    for i in range(0,n): 
        print("index :"+str(i))
        max_wrap += a[i] 
        print("max_wrap 1 :"+str(max_wrap))
        a[i] = -a[i] 
  
    # Max sum with corner elements will be: 
    # array-sum - (-max subarray sum of inverted array) 
    max_wrap = max_wrap + kadane(a) 
    print("kadane :"+str(kadane(a)))
    print("max_wrap 2 :"+str(max_wrap))
    print("max_kadane 2 :"+str(max_kadane))
    # The maximum circular sum will be maximum of two sums 
    if max_wrap > max_kadane: 
        return max_wrap 
    else:
        return max_kadane 
  
# Driver function to test above function 
a = [5,-3,5] 
print "Maximum circular sum is", maxCircularSum(a) 