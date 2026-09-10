class Solution:
    def rotate(self, matrix) :
        self.swapRows(matrix)
        self.transpose(matrix)
        return (matrix)
        
        
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n - 1):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                print ("transpose")
                print (matrix)    
                
    def swapRows(self, matrix):
        top, bottom = 0, len(matrix) - 1
        
        while(top < bottom):
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
 
            print ("swapRows")
            print (matrix)
            
            top += 1
            bottom -= 1
            

            

matrix = [[1,2,3],[4,5,6],[7,8,9]]

sol=Solution()
print (sol.rotate(matrix))

