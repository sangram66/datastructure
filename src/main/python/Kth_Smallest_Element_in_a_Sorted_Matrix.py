'''
378. Kth Smallest Element in a Sorted Matrix
Medium

4649

208

Add to List

Share
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

'''
'''
#using heap 
#Time Complexity: O(Klog(min(N,K)) or O(KlogN)

from heapq import heapify,heappush,heappop
class Solution:
    def kthSmallest(self, matrix, k) :
        rows, cols = len(matrix), len(matrix[0])
        print ("row,cols "+str(rows),str(cols ))
        heap = []
        heapify(heap)
        for i in range(min(cols, k)):
            heappush(heap, (matrix[0][i], 0, i))
            print (heap)
        
        for i in range(k-1):
            _, r, c = heappop(heap)
            print (_, r, c )
            if r+1 < rows:
                heappush(heap, (matrix[r+1][c], r+1, c))      
        
        return heappop(heap)[0]

   
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8    
print (Solution().kthSmallest(matrix,k))
''' 
#Binary Search Method
#Time Complexity: O(Nlog(max-min))
class Solution:
    def kthSmallest(self, matrix, k):
        rows, cols = len(matrix), len(matrix[0])
        minval, maxval = matrix[0][0], matrix[-1][-1]
        
        def matrixCount(num):
            count = 0
            r, c = 0, cols-1
            
            while r < rows and c >= 0:
                print ("r,c,matrix[r][c]  "+str(r),str(c),str(matrix[r][c]))
                if matrix[r][c] <= num:
                    count += c+1
                    print ("count "+str(count))
                    r += 1
                else:
                    c -= 1
            print ("\n")
            return count
        
        while minval < maxval:
            mid = (minval+maxval)//2
            print ("mid:"+str(mid))
            countl = matrixCount(mid)
            print ("countl:"+str(countl))
            if countl < k:
                minval = mid+1
            else:
                maxval = mid
        
        return maxval

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8    
print (Solution().kthSmallest(matrix,k))
