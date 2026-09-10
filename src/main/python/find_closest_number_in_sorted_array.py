'''

Find closest number in Sorted array

Examples:

Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}, target = 11
Output : 9
Explanation : 9 is closest to 11 in given array


Input :arr[] = {2, 5, 6, 7, 8, 8, 9}, target = 4
Output : 5
Explanation :5 is closest to 4 in given array


Input :arr[] = {2, 5, 6, 7, 8, 8, 9, 15, 19, 22, 32}, target = 17
Output : 19
Explanation : 15 and 19 both are closest to 17 in given array ,so return max(15, 19) which is 19

'''
def findClosest(arr, target):
    n = len(arr)
    i = 0

    # Find the first larger element of target in arr
    for i in range(1, n):
        if arr[i] >= target:
            break

    # If all elements are smaller, return the last element
    if i == n:
        return arr[n-1]

    # Check the current and previous element for closest
    if (arr[i] - target) <= target - arr[i-1]:
        return arr[i]
    else:
        return arr[i-1]

if __name__ == "__main__":
    arr = [2, 5, 6, 7, 8, 8, 9, 15, 19, 22, 32]
    target = 17
    print(findClosest(arr, target))
