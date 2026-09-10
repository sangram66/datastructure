def printMultiplicationTableFor12():
    for row in range(1, 13):
        for col in range(1, 13):
            print('{:3} '.format(row * col),end='')
        print()
    
    
printMultiplicationTableFor12()