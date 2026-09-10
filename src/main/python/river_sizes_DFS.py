'''

 
  You're given a two-dimensional array (a matrix) of potentially unequal height
  and width containing only  0 s and  1 s. Each
   0  represents land, and each  1  represents part of a
  river. A river consists of any number of  1 s that are either
  horizontally or vertically adjacent (but not diagonally adjacent). The number
  of adjacent  1 s forming a river determine its size.
 
  Note that a river can twist. In other words, it doesn't have to be a straight
  vertical line or a straight horizontal line; it can be L-shaped, for example.
 
  Write a function that returns an array of the sizes of all rivers represented
  in the input matrix. The sizes don't need to be in any particular order.
 

 Sample Input 
matrix  = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]


 Sample Output 
[1, 2, 2, 2, 5] 
// The numbers could be ordered differently. 

 // The rivers can be clearly seen here: 
 // [ 
 //   [1,  ,  , 1,  ], 
 //   [1,  , 1,  ,  ], 
 //   [ ,  , 1,  , 1], 
 //   [1,  , 1,  , 1], 
 //   [1,  , 1, 1,  ], 
 // ] 


'''




def riversizes(matrix):
    sizes=[]
    visited=[[False for value in row ] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i,j,matrix,visited,sizes)
            
    return sizes


def traverseNode(i,j,matrix,visited,sizes):
    currentRiversize=0
    nodesToExplore=[[i,j]]
    while len(nodesToExplore):
        currentNode=nodesToExplore.pop()
        i=currentNode[0]
        j=currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j]=True
        if matrix[i][j]==0:
            continue
        currentRiversize+=1
        unvisitedNeighbours=getunvisitedNeighbors(i,j,matrix,visited)
        for neighbor in unvisitedNeighbours:
            nodesToExplore.append(neighbor)
            
    if currentRiversize >0 :
        sizes.append(currentRiversize)
        
def getunvisitedNeighbors(i,j,matrix,visited):
    unvisitedneighbors=[]
    if i>0 and not visited[i-1][j]:
        unvisitedneighbors.append([i-1,j])
    if i < len(matrix)-1 and not visited[i+1][j]:
        unvisitedneighbors.append([i+1,j])
    if j>0 and not visited[i][j-1]:
        unvisitedneighbors.append([i,j-1])
    if j<len(matrix[0])-1 and not visited[i][j+1]:
        unvisitedneighbors.append([i,j+1])
        
    return unvisitedneighbors

riversize=[[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]

print (riversizes(riversize))
        