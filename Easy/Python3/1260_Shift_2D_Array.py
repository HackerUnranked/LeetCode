from typing import List

# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

# In one shift operation:

#     Element at grid[i][j] moves to grid[i][j + 1].
#     Element at grid[i][n - 1] moves to grid[i + 1][0].
#     Element at grid[m - 1][n - 1] moves to grid[0][0].

# Return the 2D grid after applying shift operation k times. 

# Example 1:

# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]

# Example 2:

# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

# Example 3:

# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        k = k % (len(grid) * len(grid[0])) # find the "real k" see explanation below
        
        # if k is a muliple of the size of the matrix then it means
        # we don't need to shift, example matrix size 9 and k is
        # 18 this means the matrix stays the same because after each
        # 9 shifts the matrix is back where it originally was
        
        while k != 0:
            # get the last item because we should swap it with the first
            prev = grid[len(grid) - 1][len(grid[0]) - 1]
            
            for row in grid:
                for x in range(len(row)):
                    temp = row[x]
                    row[x] = prev # swap with the previous
                    prev = temp # keep track of the previous
            
            k -= 1
                
        return grid