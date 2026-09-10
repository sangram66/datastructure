import itertools
import collections
class Solution(object):
    def slidingPuzzle(self, board):
        R, C = len(board), len(board[0])
        print ("R C "+str(R),str(C))
        start = tuple(itertools.chain(*board))
        print ("start "+str(start))
        queue = collections.deque([(start, start.index(0), 0)])
        print ("queue: "+str(queue))
        seen = {start}

        target = tuple([(range(1, R*C))] + [0])
        print ("target "+str(target))

        while queue:
            board, posn, depth = queue.popleft()
            print (board, posn, depth)
            if board == target: return depth
            for d in (-1, 1, -C, C):
                nei = posn + d
                print ("nei  posn c "+str(nei),str(posn),str(C))
                if abs(nei/C - posn/C) + abs(nei%C - posn%C) != 1:
                    print ("inside first if "+str(abs(nei/C - posn/C) + abs(nei%C - posn%C)))
                    continue
                if 0 <= nei < R*C:
                    newboard = list(board)
                    print ("newboard"+str(newboard))
                    newboard[posn], newboard[nei] = newboard[nei], newboard[posn]
                    print ("newboard"+str(newboard))
                    newt = tuple(newboard)
                    if newt not in seen:
                        seen.add(newt)
                        queue.append((newt, nei, depth+1))

        return -1

if __name__ == "__main__":
    sol=Solution()
    board = [[1,2,3],[4,0,5]]
    print (sol.slidingPuzzle(board))
    