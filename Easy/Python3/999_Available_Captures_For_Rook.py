from typing import List


# On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of 
# white bishops 'B', black pawns 'p', and empty squares '.'.

# When the rook moves, it chooses one of four cardinal directions:
#     (north, east, south, or west), 
# then moves in that direction until it chooses to stop, reaches the edge of the 
# board, captures a black pawn, or is blocked by a white bishop. A rook is 
# considered attacking a pawn if the rook can capture the pawn on the rook's 
# turn. The number of available captures for the white rook is the number of 
# pawns that the rook is attacking.

# Return the number of available captures for the white rook. 

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find the location of the Rook
        for x in range(len(board)):
            found = False
            for y in range(len(board[x])):
                if board[x][y] == 'R':
                    found = True
                    # we found the rook so
                    # next we need to see if there's anything blocking
                    # or if we can get a pawn
                    break
            # leave the nested loop
            if found == True:
                break
                
        # now we need to check the column and the row to see if we can get a pawn
        l = y
        r = y
        up = x
        down = x
        capture = 0
        
        # loop left
        while l >= 0:
            # we can take the pawn
            if board[x][l] == "p":
                capture += 1
                break
            # we saw a bishop
            elif board[x][l] == 'B':
                break
            
            l -= 1
        
        # loop right
        while r < len(board[x]):
             # we can take the pawn
            if board[x][r] == "p":
                capture += 1
                break
            # we saw a bishop
            elif board[x][r] == 'B':
                break
            
            r += 1
        
        # loop up
        while up >= 0:
            if board[up][y] == 'p':
                capture += 1
                break
            elif board[up][y] == 'B':
                break
                
            up -= 1
        
        # loop down
        while down < len(board[x]):
            if board[down][y] == 'p':
                capture += 1
                break
            elif board[down][y] == 'B':
                break
            
            down += 1
            
        return capture