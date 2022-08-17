from typing import List

# You are given row x col grid representing a map where grid[i][j] = 1 
# represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is 
# completely surrounded by water, and there is exactly one island 
# (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to 
# the water around the island. One cell is a square with side length 1. The grid 
# is rectangular, width and height don't exceed 100. Determine the perimeter of 
# the island.

# Example 1:

# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Example 2:

# Input: grid = [[1]]
# Output: 4

# Example 3:

# Input: grid = [[1,0]]
# Output: 4

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        
        for row_num, row in enumerate(grid):
            for col_num, col in enumerate(row):
                # check if there are any other pieces of the are
                # next to the island piece
                if col == 1:
                    total = 4
                    # check right
                    if col_num < len(row) - 1 and row[col_num + 1] == 1:
                        total -= 1
                    # check left
                    if col_num > 0 and row[col_num - 1] == 1:
                        total -= 1
                    # check above me
                    if row_num > 0 and grid[row_num - 1][col_num] == 1:
                        total -= 1
                    # check below me
                    if row_num < len(grid) - 1 and grid[row_num + 1][col_num] == 1:
                        total -= 1
                    
                    perimeter += total
                    
        return perimeter
                            