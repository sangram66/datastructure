'''
Min Number Of Jumps

You are given a non-empty array of integers. Each element represents the maximum number of steps you can take forward. For example, if the element at index 1 is 3, you can go from index 1 to index 2, 3, or 4. Write a function that returns the minimum number of jumps needed to reach the final index. Note that jumping from index i to index i + x always constitutes 1 jump, no matter how large x is.

Sample input: [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
Sample output: 4 (3 --> 4 or 2 --> 2 or 3 --> 7 --> 3)

'''

# O(n^2) time | O(n) space
def minNumberOfJumps(array):
    jumps = [float("inf") for x in array]
    print(jumps)
    jumps[0] = 0
    print(jumps)
    for i in range(1, len(array)):
        for j in range(0, i):
            print ("array:" +str(array))
            print ("array[j],i,j "+str(array[j]),str(i),str(j))
            if array[j] >= i - j:
                print("jumps0: "+str(jumps))
                jumps[i] = min(jumps[j] + 1, jumps[i])
                print("jumps1: "+str(jumps))
    return jumps[-1]

arr=[3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
print (minNumberOfJumps(arr))
