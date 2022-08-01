# There is a robot starting at the position (0, 0), the origin, on a 2D plane. 
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it 
# completes its moves.

# You are given a string moves that represents the move sequence of the robot 
# where moves[i] represents its ith move. Valid moves are 'R' (right), 
# 'L' (left), 'U' (up), and 'D' (down).

# Return true if the robot returns to the origin after it finishes all of its 
# moves, or false otherwise.

# Note: The way that the robot is "facing" is irrelevant. 'R' will always make 
# the robot move to the right once, 'L' will always make it move left, etc. 
# Also, assume that the magnitude of the robot's movement is the same for each 
# move.

# Example 1:

# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the 
# same magnitude, so it ended up at the origin where it started. Therefore, we 
# return true.

# Example 2:

# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of 
# the origin. We return false because it is not at the origin at the end of its 
# moves.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # coordinates to keep track of the movements
        x = 0
        y = 0
        
        for move in moves:
            # a move right means the x coordinate increases by 1
            if move == 'R':
                x += 1
            # a move left means the x coordinate decreases by 1
            if move == 'L':
                x -= 1
            # a move up means the y coordinate increases by 1
            if move == 'U':
                y += 1
            # a move down mean the y coordinate decreases by 1
            if move == 'D':
                y -= 1
                
        # if the y and x are both 0 then we returned to the origin
        if x == 0 and y == 0:
            return True
        
        return False