from typing import List

class Solution:    
    def tictactoe(self, moves: List[List[int]]) -> str:
        Rows = [[0,0,0],[0,0,0]]
        Col = [[0,0,0],[0,0,0]]
        diag = [0,0]
        
        player_a = True
        
        for move in moves:
            
            if player_a:
                
                print("player a's turn")
                player_a = False
                Rows[0][move[0]] += 1
                Col[0][move[1]] += 1

                print("adding values")
                print(Rows[0],Col[0]) 
                # if the coordinates are equal it's part of the diagonal
                if move[0] == move[1]:
                    diag[0] += 1
                
                if move[0] == 2 - move[1]:
                    diag[1] += 1
            else:
                print("player b's turn")
                player_a = True
                Rows[1][move[0]] += 1
                Col[1][move[1]] += 1
                
                # if the coordinates are equal it's part of the diagonal
                if move[0] == move[1]:
                    diag[0] -= 1
                
                if move[0] == 2 - move[1]:
                    diag[1] -= 1
                
        
        if diag[0] == 3 or diag[1] == 3:
            return "A"
        
        # did B get a diagonal?
        if diag[1] == -3 or diag[0] == -3:
            return "B"
        
        # check if A get a or column
        if 3 in Rows[0] or 3 in Col[0]:
            return "A"
        
        # check if B got a row or column
        if 3 in Rows[1] or 3 in Col[1]:
            return "B"
        
        # this means there are more moves but they are done playing
        if len(moves) < 9:
            return "Pending"
        