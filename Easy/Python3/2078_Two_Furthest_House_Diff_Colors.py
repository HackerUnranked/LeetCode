from typing import List

# There are n houses evenly lined up on the street, and each house is 
# beautifully painted. You are given a 0-indexed integer array colors of length 
# n, where colors[i] represents the color of the ith house.

# Return the maximum distance between two houses with different colors.

# The distance between the ith and jth houses is abs(i - j), where abs(x) is the 
# absolute value of x. 

# Example 1:

# Input: colors = [1,1,1,6,1,1,1]
# Output: 3
# Explanation: In the above image, color 1 is blue, and color 6 is red.
# The furthest two houses with different colors are house 0 and house 3.
# House 0 has color 1, and house 3 has color 6. The distance between them is 
# abs(0 - 3) = 3.
# Note that houses 3 and 6 can also produce the optimal answer.

# Example 2:

# Input: colors = [1,8,3,8,3]
# Output: 4
# Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 
# 3 is green. The furthest two houses with different colors are house 0 and 
# house 4. House 0 has color 1, and house 4 has color 3. The distance between 
# them is abs(0 - 4) = 4.

# Example 3:

# Input: colors = [0,1]
# Output: 1
# Explanation: The furthest two houses with different colors are house 0 and 
# house 1. House 0 has color 0, and house 1 has color 1. The distance between 
# them is abs(0 - 1) = 1.

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # the first item and last item will be used
        # to calculate the distance because they are the
        # furthest distance from all the other items in the list.
        #
        # first take the first item and find the last item that is not the same
        # as it.
        #
        #
        # next do the same with the last item while traversiving backwards from the list
        #
        # special cases are if all the items in the list are the same then we return 0
        #
        # return the max of the first item or last item
        
        # if the first and last item are differen then they
        # are the furthest from each other and no need to loop
        # return the distance
        if colors[0] != colors[len(colors) - 1]:
            return len(colors) - 1
        
        idx = 0
        idx2 = 0
        
        a = colors[len(colors) - 1] # value of last item
        b = colors[0] # value of first item
        
        # loop right
        for x, y in enumerate(colors):
            if b != y:
                idx = x
                
        # all the numbers were the same return zero
        if 0 == idx:
            return 0
        
        # loop from right to left
        for x in range(len(colors) -1, -1, -1):
            if a != colors[x]:
                idx2 = x

        return max(idx, abs(len(colors) - idx2 - 1))
                