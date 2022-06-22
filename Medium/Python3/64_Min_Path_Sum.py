from typing import List

# Given a m x n grid filled with non-negative numbers, find a path from top left
# to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:

# [1,3,1]
# [1,5,1]
# [4,2,1]

# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:
#
# [1,2,3]
# [4,5,6]
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

 


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if len(grid) == 0:
            return 0
        
        # NOTE: we for loop the entire matrix and add the values along the path 
        # we took to get to the current coordinates. Since we can only move
        # right and down this means wherever we are we either came from above
        # or to the left.
        
        for row in range(len(grid)):
            # NOTE: since this is not an NxN matrix but an MxN we that means
            # we loop the size of the row which is the length of a list instead of
            # using the size of the column
            for column in range(len(grid[0])):
                
                # this means we are in the middle and
                # we can come from the left or above since we
                # can only move right and down. Take the min and add it
                if row > 0 and column > 0:
                    grid[row][column] += min(grid[row - 1][column], grid[row][column -1])
                
                # this means we came from above since column is 0 which is the beginning
                # so we couldn't have came from the left. add the above val to where we are at
                elif row > 0:
                    grid[row][column] += grid[row - 1][column]
                
                # we are row 0 meaning we can only come from the left
                # since there is no top row to come from
                elif column > 0:
                    grid[row][column] += grid[row][column - 1]
                    
        # return the result
        return grid[len(grid) - 1][len(grid[0]) - 1]