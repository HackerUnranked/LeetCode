from typing import List

# Given an m x n binary matrix mat, return the number of special positions in 
# mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements 
# in row i and column j are 0 (rows and columns are 0-indexed).

# Example 1:

# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other 
# elements in row 1 and column 2 are 0.

# Example 2:

# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # a cell is unique if it's a one and only appears
        # once in the row and column
        
        row_count = [0] * len(mat)
        col_count = [0] * len(mat[0])
        res = 0
        
        # count the number of 1s we see in each row and column
        for idx, row in enumerate(mat):
            for idx2, val in enumerate(row):
                if val == 1:
                    # map the one to it's row and column
                    row_count[idx] += 1
                    col_count[idx2] += 1
        
        # if the cell is a one check if there is only
        # one value in the same row and column, add one
        # if so otherwise skip it
        for i in range(len(row_count)):
            for j in range(len(col_count)):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    res += 1
        
        return res
       
            