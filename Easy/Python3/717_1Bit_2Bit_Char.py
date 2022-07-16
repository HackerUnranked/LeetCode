from typing import List

# We have two special characters:

#     The first character can be represented by one bit 0.
#     The second character can be represented by two bits (10 or 11).

# Given a binary array bits that ends with 0, return true if the last character
# must be a one-bit character.

# Example 1:

# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.

# Example 2:

# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit character.
# So the last character is not one-bit character.

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
   
        idx = 0
        oneBit = False

        # loop the list using look-ahead approach 
        while idx < len(bits):
            # move bits over 2 if we seen a 1 and
            # set the oneBit to true because it this
            # means it has to be a 2 bit char
            if bits[idx] == 1:
                idx += 2 
                oneBit = False
            # move bits over by 1 if we seen a zero because 
            # this means it has to be a 1 bit char
            else:
                oneBit = True
                idx += 1
        
        return oneBit # return 