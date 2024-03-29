from typing import List

# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        for x in range(len(matrix)):
            small = matrix[x][0] # helps us find the smallest value
            the_idx = 0 # idx so we know which column to look 
            
            # find the smallest value
            for idx,val in enumerate(matrix[x]):
                if small > val:
                    small = val
                    the_idx = idx
            
            big = 0 # to find the biggest
            
            # loop the column to find the biggest
            for cols in matrix:
                if cols[the_idx] > big:
                    big = cols[the_idx]
                    
            # compare the biggest val in col with smallest in row and return if they are the same
            if big == small:
                return [small]