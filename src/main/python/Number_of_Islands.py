
class Solution(object):
    def numIslands(self, grid):
        islands = 0
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    print ("inside numIslands")
                    print ("i,j:"+str(i)+','+str(j))
                    print ("islands:"+str(islands))
                    self.part_of_island(i,j,grid)
        return islands

    def part_of_island(self, i, j,grid):
        print ("inside part_of_island")
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            print ("i,j:"+str(i)+','+str(j))
            return
        else:
            grid[i][j] = '0'
        print ("**********************")
        print ("calling part 1: "+str(i)+','+str(j+1)) 
        print ("Actual i j: "+str(i)+','+str(j))   
        self.part_of_island(i,j+1,grid)
        
        
        print ("**********************")
        print ("calling part 4: "+str(i-1)+','+str(j))
        print ("Actual i j: "+str(i)+','+str(j))  
        self.part_of_island(i-1,j,grid)          
        
        print ("**********************")
        print ("calling part 3: "+str(i+1)+','+str(j))
        print ("Actual i j: "+str(i)+','+str(j))  
        self.part_of_island(i+1,j,grid)
        
        print ("**********************")
        print ("calling part 2: "+str(i)+','+str(j-1)) 
        print ("Actual i j: "+str(i)+','+str(j))   
        self.part_of_island(i,j-1,grid)
        

        
if __name__=='__main__':
    sol=Solution()
    # grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    #grid=[[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
    grid=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print ("grid")
    print (grid)
    res=sol.numIslands(grid)
    print (res)
