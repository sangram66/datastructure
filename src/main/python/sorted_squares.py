
class Solution(object):
    def sortedSquares(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1
        print ('i '+str(i))
        print ('j '+str(j))

        ans = []
        while 0 <= i and j < N:
            print (A[i],A[j])
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                print (' inside first while if ans '+str(ans))
                i -= 1
            else:
                ans.append(A[j]**2)
                print (' inside first while else ans '+str(ans))
                j += 1
                
        print (' first while ans '+str(ans))

        while i >= 0:
            ans.append(A[i]**2)
            print (' second while ans '+str(ans))
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            print (' third while ans '+str(ans))
            j += 1

        return ans
    
#print(Solution().sortedSquares([-4,-1,0,3,10,7,9]))
print(Solution().sortedSquares([-8,-4,-1,0,3,7,9,10]))
