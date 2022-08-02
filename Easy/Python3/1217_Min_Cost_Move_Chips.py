from typing import List

# We have n chips, where the position of the ith chip is position[i].

# We need to move all the chips to the same position. In one step, we can change 
# the position of the ith chip from position[i] to:

#    position[i] + 2 or position[i] - 2 with cost = 0.
#    position[i] + 1 or position[i] - 1 with cost = 1.

# Return the minimum cost needed to move all the chips to the same position. 

# Example 1:

# Input: position = [1,2,3]
# Output: 1
# Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
# Second step: Move the chip at position 2 to position 1 with cost = 1.
# Total cost is 1.

# Example 2:

# Input: position = [2,2,2,3,3]
# Output: 2
# Explanation: We can move the two chips at position  3 to position 2. Each move 
# has cost = 1. The total cost = 2.

# Example 3:
# Input: position = [1,1000000000]
# Output: 1

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0 # count the evens
        odd = 0 # count the odds
        
        # loop and count how many evens vs odds
        for chip in position:
            if chip % 2 == 0:
                even += 1
            else:
                odd += 1
        # return the smaller of the two
        return min(even, odd)
    
    # given a chip with a number even or odd, the moves costs the folowing
    #
    # cost chart:
    #  even -> odd = +1 cost becase we have to move 1, even - 1 = odd number
    #  even -> even = free because moves has no cost for 2x moves, even + 2 = even number
    #  odd -> even = +1 because to ge to an even from an odd we have to do 2x + 1, odd - 1 = even
    #  odd -> odd  = free since odd + 2 is odd and 2x moves is free, odd + 2 = odd
    #  
    # judging from the following rules we count the number of odd and even numbers then return the lesser
    # of the two
    #
    # x even means we need x moves to get to and odd number y because 2x + 1 gives us the odd number where x
    # is free since we can move 2 moves for free but the +1 costs us 1.
    #
    # y is odd means we need y moves to get to even similaryly as above it costs us +1
    #
    # example: a = [1,1,1,4,4]
    # we return 2 because it will cost us +2 since there are 2 even numbers and even appears less than odds
    #
    # example b = [3,3,3,6,6,6,6]
    #
    # return 3 because we have less odds and need 3 moves per 3's to get to 6 after 3 + 2(free) = 5