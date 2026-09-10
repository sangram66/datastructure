'''
def spiralmatrix(array):
    if not array:
        return []
    startrow,endrow=0,len(array)-1
    startcol,endcol=0,len(array[0])-1
    results=[]
    while startrow <= endrow and startcol <= endcol:
        for col in range(startcol,endcol+1):
            print (col)
            results.append(array[startrow][col])
            print (results)
        
        for row in range(startrow+1,endrow+1):
            results.append(array[row][endcol])
        
        for col in reversed(range(startcol,endcol)):
            if startrow == endrow:
                break
            else:
                results.append(array[endrow][col])
        
        for row in reversed(range(startrow+1,endrow)):
            if startcol==endcol:
                break
            else:
                results.append(array[row][startcol])
                
        startrow+=1
        endrow-=1
        startcol+=1
        endcol-=1
    return results

#array=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
array=[[1,2,3],[4,5,6],[7,8,9]]
#array=[]
print (spiralmatrix(array))
'''

class Solution:
    def spiralOrder(self, matrix) :
        result = list()
        while len(matrix) > 0:
            try:
                result += matrix.pop(0) #remove the first nested list (top row)
                result += [x.pop(-1) for x in matrix] #remove every last element of the lists (right row)                                                            
                result += matrix.pop(-1)[::-1] #remove last nested list in reverse order (bottom row)
                print (result)
                print ([x.pop(0) for x in matrix][::-1])
                result += [x.pop(0) for x in matrix][::-1] #remove every last element of the lists (left row)
            except:
                break #if at any moment the matrix is empty, break the loop and return the result array
        return result
    
#array=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
array=[[1,2,3],[4,5,6],[7,8,9]]
#array=[]
print (Solution().spiralOrder(array))
