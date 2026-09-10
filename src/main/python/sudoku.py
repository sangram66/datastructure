#https://leetcode.com/explore/interview/card/apple/348/others/3141/
'''
class Solution:
    def isValidSudoku(self, board) :
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                char=board[r][c]
                print (char)
                if char != ".":
                    if char not in row[r]:
                        row[r]=char
                        #print (row)
                    else:
                        print ("row1")
                        return False
                    if char not in col[c]:
                        col[c]=char
                        #print (col)
                    else:
                        print ("col1")
                        return False
                    
                    boxidx=(r//3)*3 + c//3
                    if char not in box[boxidx]:
                        box[boxidx]=char
                        print (box)
                    else:
                        print ("box1")
                        return False 
                    
        return True
'''

class Solution:
    box_size = 3
    board_size = 9
    
    def rowsValid(self, board):
        # check each row
        for r in board:
            seen = set()
            for item in r:
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)
        return True
    
    def colsValid(self, board):
        # check each column
        for i in range(self.board_size):
            seen = set()
            for r in board:
                if r[i] in seen:
                    return False
                elif r[i] != '.':
                    seen.add(r[i])
        return True
    
    def boxesValid(self, board):
        # check each box
        for boxx in range(0, self.board_size, self.box_size):
            for boxy in range(0, self.board_size, self.box_size):
                seen = set()
                for x in range(self.box_size):
                    row = board[boxx + x]
                    for y in range(self.box_size):
                        item = row[boxy + y]
                        if item in seen:
                            return False
                        elif item != '.':
                            seen.add(item)
        return True
    
    def isValidSudoku(self, board) -> bool:
        return self.rowsValid(board) and self.colsValid(board) and self.boxesValid(board)
        
Input=[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
   
print (Solution().isValidSudoku(Input))     
