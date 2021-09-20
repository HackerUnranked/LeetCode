from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        to_return = []
        
        if len(matrix) == 0:
            return None
        
        topRow = 0 # -->
        bottomRow = len(matrix) - 1 # going down
        leftRow = 0 # going left
        rightRow = len(matrix[0]) - 1 # going right
        matrix_size = len(matrix) * len(matrix[0]) # how many items is in the matrix
        
        # Note, we need to check the to_return < matrix size in each loop 
        # we are constantly adding an element to the list
        # this prevents us from adding and looping
        # if we haven't visited all the items then keep looping and add
        # items to the list
        while len(to_return) < matrix_size:
            
            counter = leftRow # we start at left to get the top row
            # get the top row by starting left and going right 
            while counter <= rightRow:
                print("going right top adding ", matrix[topRow][counter])
                to_return.append(matrix[topRow][counter]) # append the item
                counter = counter + 1 # moving over 1 to look at top row from left to right 
        
            # move the top row down 1 so we can get the far right row going down
            topRow = topRow + 1
            
            # now look at the bottom column going down
            counter = topRow
            
            # we loop and stop right before the bottom row to get the far right elements
            while counter <= bottomRow and len(to_return) < matrix_size:
                print("going down right adding ", matrix[counter][rightRow])
                to_return.append(matrix[counter][rightRow]) 
                counter = counter + 1 # move down the elements in the last column in the far right
            
            rightRow = rightRow - 1 # move the right row because we looked at one already
            
            counter = rightRow
            # get the last row before going up again 
            while counter >= leftRow and len(to_return) < matrix_size:
                print("going left bottom ", matrix[bottomRow][counter])
                to_return.append(matrix[bottomRow][counter]) # get all the elements on the bottom row starting from right to left
                counter = counter - 1
            
            bottomRow = bottomRow - 1
            
            counter = bottomRow
            while counter >= topRow and len(to_return) < matrix_size:
                print("going up bottom adding ", matrix[counter][leftRow])
                to_return.append(matrix[counter][leftRow]) # go up to get the remaining elements to complete the matrix spiral
                counter = counter - 1
            
            leftRow = leftRow + 1
            print(len(to_return))
            print(to_return)
            print(matrix_size)
        
        return to_return 