''''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Time Complexity: O(k log d + d), where d is the count of distinct elements in the array. 
To remove the top of priority queue O(log d) time is required, so if k elements are removed then O(k log d) time is required and to traverse the distinct elements O(d) time is required.
Auxiliary Space: O(d), where d is the count of distinct elements in the array. 
To store the elements in HashMap O(d) space complexity is needed.


'''''





# Python3 implementation to find k
# numbers with most occurrences in
# the given array
import heapq
 
# Function to print the k numbers with
# most occurrences
def print_N_mostFrequentNumber(arr, n, k):
     
    mp = dict()
     
    # Put count of all the distinct elements
    # in dictionary with element as the
    # key & count as the value.
    for i in range(0, n):
        if arr[i] not in mp:
            mp[arr[i]] = 1
        else:
            mp[arr[i]] += 1
             
    # Using heapq data structure
    heap = [(value, key) for key,
             value in mp.items()]
    print (heap)
              
    # Get the top k elements
    largest = heapq.nlargest(k, heap)
    print (largest)
 
    # Insert the data from the map to
    # the priority queue
    print(k, " numbers with most "
             "occurrences are:", sep = "")
              
    # Print the top k elements
    for i in range(k):
        print(largest[i][1], end =" ")
 
# Driver code
if __name__=="__main__":
     
    arr = [ 3, 1, 4, 4, 5, 2, 6, 1 ]
    n = len(arr)
    k = 2
     
    print_N_mostFrequentNumber(arr, n, k)
     
# This code is contributed by MuskanKalra1