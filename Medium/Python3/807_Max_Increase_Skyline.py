from typing import List

# There is a city composed of n x n blocks, where each block contains a single 
# building shaped like a vertical square prism. You are given a 0-indexed n x n 
# integer matrix grid where grid[r][c] represents the height of the building 
# located in the block at row r and column c.

# A city's skyline is the the outer contour formed by all the building when 
# viewing the side of the city from a distance. The skyline from each cardinal 
# direction north, east, south, and west may be different.

# We are allowed to increase the height of any number of buildings by any amount 
# (the amount can be different per building). The height of a 0-height building 
# can also be increased. However, increasing the height of a building should not 
# affect the city's skyline from any cardinal direction.

# Return the maximum total sum that the height of the buildings can be increased 
# by without changing the city's skyline from any cardinal direction. 

# Example 1:

# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation: The building heights are shown in the center of the above image.
# The skylines when viewed from each cardinal direction are drawn in red.
# The grid after increasing the height of buildings without affecting skylines is:
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

# Example 2:

# Input: grid = [[0,0,0],[0,0,0],[0,0,0]]
# Output: 0
# Explanation: Increasing the height of any building will result in the skyline 
# changing.

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # Question is asking what is the sum of changing a value in the matrix
        # to equal the min(max(row,col))
        #
        # Example:
        
        # [[3,0,8,4],
        #  [2,4,5,7],
        #  [9,2,6,3],
        #  [0,3,1,0]]
        #
        # becomes...
        #
        #  [[8, 4, 8, 7],
        #   [7, 4, 7, 7],
        #   [9, 4, 8, 7],
        #   [3, 3, 3, 3]]
        #
        # [0][0] is 8 because in row 0, 8 is the max and 9 is the max in column 0 so
        # we take the smaller of the two which is 8, 8 - 3 = 5. we need to increase
        # [0][0] by 5 to get 8, add this to the sum and repeat for the rest of the
        # values in the matrix

        # rotate the array so we can check the columns
        flipped = list(zip(*grid))
        
        num = 0 # count the max change we can make
        
        for idx in range(len(grid)):
            for idx2 in range(len(grid)):
                # this is the max height we can change the integer
                a = min(max(grid[idx]), max(flipped[idx2]))
                # if the grid val is smaller than the max height then we count the difference
                if grid[idx][idx2] < a:
                    num += a - grid[idx][idx2]
                
        return num