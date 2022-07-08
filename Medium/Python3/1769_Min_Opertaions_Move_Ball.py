from typing import List

# You have n boxes. You are given a binary string boxes of length n, where 
# boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

# In one operation, you can move one ball from a box to an adjacent box. Box i 
# is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may 
# be more than one ball in some boxes.

# Return an array answer of size n, where answer[i] is the minimum number of 
# operations needed to move all the balls to the ith box.

# Each answer[i] is calculated considering the initial state of the boxes.

# Example 1:

# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first 
#    box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second
#    box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third 
#    box in two operations, and move one ball from the second box to the third 
#    box in one operation.

# Example 2:

# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n # create an array of size n to store the min number of operation
        curr, steps = 0, 0
        
        # calculate from left to right how many moves it takes to move 1 ball to the current idx
        for i in range(1,n):
            curr += int(boxes[i-1]) # get the previous idx value
            steps += curr # add it to the steps
            answer[i] += steps # increment the idx by the steps
        
        # NOTE from the above it all idx are 1's on the left:
        # a = [1, 1, 1, 1]
        #
        # after the first iteration it will be
        # curr = 1
        # steps = 1
        # n = [0, 1, 0, 0] because it takes 1 itertaion to move the left to idx 1
        #
        # second iteration
        # current = 2
        # steps = 3
        # n = [0, 1, 3, 0] because steps is 3
        #
        #
        # third
        #
        # current = 3
        # steps = 6
        # n = [0, 1, 3, 6] This is the final on how many moves it takes to move a 1 from the lef to right, now we need to do the same for
        # moving from the right to left below
        
        curr, steps = 0, 0
        
        for i in reversed(range(n-1)):
            curr += int(boxes[i+1])
            steps += curr
            answer[i] += steps
        
        # n = [0, 1, 3, 6]
        #
        # after the first iteration
        # cur = 1
        # steps = 1
        # n = [0, 1, 4, 6]
        #
        # second iteration
        #
        # cur = 2
        # step = 3
        # n = [0, 4, 4, 6]
        #
        #
        # cur = 3
        # step = 6
        # n = [6, 4, 4, 6]
        
        return answer