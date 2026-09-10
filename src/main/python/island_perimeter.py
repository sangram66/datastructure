#https://leetcode.com/problems/island-perimeter/
class Solution(object):
    def islandPerimeter(self, grid):
        sum1 = 0
        for rowind in range(0,len(grid)):
            for colind in range(0,len(grid[0])):
                if grid[rowind][colind]==1:
                    sum1+=4
                    if rowind>0 and grid[rowind-1][colind] == 1:
                        sum1-=2
                    if colind>0 and grid[rowind][colind-1] == 1:
                        sum1-=2
        return sum1
grid=[[0,1,0,0], [1,1,1,0], [0,1,0,0],[1,1,0,0]]
sol=Solution()
print (sol.islandPerimeter(grid))