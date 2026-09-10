'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1


'''
class Solution(object):
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(Solution().longestIncreasingPath(matrix))

'''
def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

    # corner case
    if not matrix or not matrix[0]:
        return 0

    # initilization
    M, N = len(matrix), len(matrix[0]) # length, width
    dp = [[0]*N for i in range(M)] # 2-D matrix for store the number of steps

    # dfs function
    def dfs(i, j):
        if not dp[i][j]: # if this position is not visited
            val = matrix[i][j]
            # search four directions to find out the decreasing path
            # up
            if i and val > matrix[i-1][j]:
                up = dfs(i-1, j)
            else:
                up = 0
            # down
            if i < M-1 and val > matrix[i+1][j]:
                down = dfs(i+1, j)
            else:
                down = 0
            # left
            if j and val > matrix[i][j-1]:
                left = dfs(i, j-1)
            else:
                left = 0
            # right
            if j < N-1 and val > matrix[i][j+1]:
                right = dfs(i, j+1)
            else:
                right = 0
            # "walk" to the target neighbor and accumulate the number of steps
            dp[i][j] = 1 + max(up, down, left, right)
        return dp[i][j]

    res_path = []
    for x in range(M): # search the grid by dfs
        for y in range(N):
            res_path.append(dfs(x, y))

    return max(res_path)
'''