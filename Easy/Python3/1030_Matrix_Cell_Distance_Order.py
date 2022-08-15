from typing import List

# You are given four integers row, cols, rCenter, and cCenter. There is a 
# rows x cols matrix and you are on the cell with the coordinates 
# (rCenter, cCenter).

# Return the coordinates of all cells in the matrix, sorted by their distance 
# from (rCenter, cCenter) from the smallest distance to the largest distance. 
# You may return the answer in any order that satisfies this condition.

# The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|. 

# Example 1:

# Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
# Output: [[0,0],[0,1]]
# Explanation: The distances from (0, 0) to other cells are: [0,1]

# Example 2:

# Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
# Output: [[0,1],[0,0],[1,1],[1,0]]
# Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
# The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

# Example 3:

# Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
# Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
# There are other answers that would also be accepted as correct, such as 
# [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        count = 0 # count how many cells we have so we can stop
        dic = defaultdict(list) # keeps track of the distances
        a = []
        
        # loop count the cels and determine the coordinate from the cell number
        while count != cols * rows:
            row_coord = count // cols # this gives us the row number
            col_coord = count % cols # this gives us the col number
            diff = abs(row_coord - rCenter) + abs(col_coord - cCenter) # get the distance of two points
            
            # add the points to the list
            dic[diff].append([row_coord, col_coord])
            
            count += 1
            
        # sort the keys and append the values
        for i in sorted(dic.keys()):
            a.extend(dic[i])
            
        return a