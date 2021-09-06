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
        
        if len(matrix) == 0:
            return None
        
        lucky = []
        
        for rows in matrix:
            # get the minimum in the row
            min_num = min(rows)
            found = True
            # loop the row and find the index of the min number
            for i,num in enumerate(rows):
                # we found the number we need to compare
                if min_num == num:
                    # loop each column at that index
                    for col in matrix:
                        # if the number is bigger than the min in the column then we leave because
                        # it is not a lucky number
                        if col[i] > min_num:
                            found = False
                            break
            # if the num is the biggest in the column and the smallest in the row then it is a lucky number
            # add it to the array
            if found == True:
                lucky.append(min_num)
        
        return lucky