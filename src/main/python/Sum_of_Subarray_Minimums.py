class Solution:
    def sumSubarrayMins(self, A):
        A = [0]+A
        print (A)
        result = [0]*len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop() 
            j = stack[-1]
            print ("j,(i-j)*A[i]:-"+str(j),str((i-j)*A[i]))
            result[i] = result[j] + (i-j)*A[i]
            print (result)
            stack.append(i)
            print (stack)
        return sum(result) % (10**9+7)
    

arr = [3,1,2,4]
print (Solution().sumSubarrayMins(arr))