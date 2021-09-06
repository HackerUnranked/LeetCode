from typing import List

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0

# Example 3:

# Input: grid = [[1,-1],[-1,-1]]
# Output: 3

# Example 4:

# Input: grid = [[-1]]
# Output: 1

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        new_list = []
        
        for x in grid:
            new_list.extend(x)
        
        big_zero = 0
        
        for y in new_list:
            if y < 0:
                big_zero += 1
        
        return big_zero
        