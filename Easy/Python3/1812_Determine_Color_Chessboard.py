# You are given coordinates, a string that represents the coordinates of a 
# square of the chessboard. Below is a chessboard for your reference.

# Return true if the square is white, and false if the square is black.

# The coordinate will always represent a valid chessboard square. The coordinate 
# will always have the letter first, and the number second.

# Example 1:

# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is 
# black, so return false.

# Example 2:

# Input: coordinates = "h3"
# Output: true
# Explanation: From the chessboard above, the square with coordinates "h3" is 
# white, so return true.

# Example 3:

# Input: coordinates = "c7"
# Output: false

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        # for characters a,c,e,g they have the same pattern and
        # start out as black so if the coord num is even then
        # the color has to be white therefore return True otherwise
        # return false. This is the opposite for b,d,f,h. They start
        # # out as white and an even coord num indicates black therefore
        # return false
        
        if coordinates[0] == 'a' or coordinates[0] == 'c' or coordinates[0] == 'e' or coordinates[0] == 'g':
            if int(coordinates[1])  % 2 == 0:
                return True
            else:
                return False
        
        if coordinates[0] == 'b' or coordinates[0] == 'd' or coordinates[0] == 'f' or coordinates[0] == 'h':
            if int(coordinates[1])  % 2 == 0:
                return False
            else:
                return True