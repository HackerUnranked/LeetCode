from typing import List

# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the 
# elements on the secondary diagonal that are not part of the primary diagonal.

# Example 1:

# Input: mat = [[1,2,3],
#              [4,5,6],
#              [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

# Example 2:

# Input: mat = [[1,1,1,1],
#              [ 1,1,1,1],
#              [ 1,1,1,1],
#              [ 1,1,1,1]]
#Output: 8

#Example 3:

# Input: mat = [[5]]
# Output: 5

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        left_row = 0
        left_col = len(mat[0]) -1
        right_row = 0
        right_col = 0
        the_sum = 0
        
        for point in mat:
            if (right_row == left_row) and (right_col == left_col):
                the_sum += mat[right_row][right_col]
            else:
                the_sum += mat[right_row][right_col]
                the_sum += mat[left_row][left_col]

            right_row += 1
            right_col += 1
            left_row += 1
            left_col -= 1
        
        return the_sum