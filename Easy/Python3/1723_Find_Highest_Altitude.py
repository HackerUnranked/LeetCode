from typing import List

# There is a biker going on a road trip. The road trip consists of n + 1 points 
# at different altitudes. The biker starts his trip on point 0 with altitude 
# equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain 
# in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the 
# highest altitude of a point.
 
# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# Example 2:

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev = 0 # holds the sum of the altitudes
        amount = 0 # gets the max altitudes
        
        # Input: gain = [-5,1,5,0,-7]
        # Output: 1
        # Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
        # starting from 0 that is our first value there is no altitude
        # from 0 to -5 we get 0 + - 5 = -5 now we have a max is 0
        # next is -5 + 1 = -4, max is still 0
        # next is -4 + 5 = 1, max is now 1 because 1 > 0
        # next is 1 + 0 = 1, max is still 1
        # next is 1 + -7 = -6, max is still 1
        # return 1 because it is the max altitude
        
        
        # loop the array of altitudes
        for x in range(0, len(gain)):
            
            prev += gain[x] # increment each altitude
            amount = max(amount, prev) # take the max of the altitude
            
        return amount # return the max