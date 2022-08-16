from typing import List

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above 
# it as shown: 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]] # the base case
        # pascal triangle each level of row has 1 more item than the 
        # previous row. We use the first loop to create the new
        # by incrementing the row by 1 to get it bigger than the previous
        for r in range(1, numRows):
            rows.append([1] * (r+1)) # creates the new row which is 1 greater than the previous
            # this is to populate the items in the row, we stop right before
            # the end of the row because the one above it is size - 1 of
            # the current and we only need to populate the ones in the middle
            for c in range(1, r):
                # add the previous row column together with the one next to it
                rows[r][c] = rows[r-1][c] + rows[r-1][c-1]
        # return the row
        return rows 