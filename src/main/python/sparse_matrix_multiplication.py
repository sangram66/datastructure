def sparse_multi(A,B):
    r1,c1=len(A),len(A[0])
    r2,c2=len(B),len(B[0])
    res=[[0 for j in range(c2)] for i in range(r1)]
    print (res)
    dicX,dicY=[dict() for i in range(r1)],[dict() for i in range(c2)]
    
    for i in range(r1):
        for j in range(c1):
            if A[i][j] != 0 :
                dicX[i][j]=A[i][j]
                
    print (dicX)
                
    
    for i in range(r2):
        for j in range(c2):
            if B[i][j] != 0 :
                # watchout (j,i)
                dicY[j][i] =B[i][j]
                
    print (dicY)
                
    
    for i in range(r1):
        for j in range(c2):
            for val in dicX[i]:
                if val in dicY[j]:
                    res[i][j]+=dicX[i][val]*dicY[j][val]
                    
    return res

A = [
  [ 1, 2, 3],
  [4, 5, 6]
]

B = [
  [ 7, 8],
  [ 9, 10],
  [ 11,12]
]
   
print (sparse_multi(A,B))         
'''           
dicX = [{0: 1, 1: 2, 2: 3}, {0: 4, 1: 5, 2: 6}]
dicY=[{0: 7, 1: 9, 2: 11}, {0: 8, 1: 10, 2: 12}]
'''